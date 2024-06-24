import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer,\
                        BlipProcessor, BlipForConditionalGeneration, \
                        MBartModel, AutoTokenizer


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class Translator():
    def __init__(self) -> None:
        self.model_name = 'utrobinmv/t5_translate_en_ru_zh_large_1024'
        self.model = T5ForConditionalGeneration.from_pretrained(self.model_name).to(device)
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        
    def translate(self, input: str) -> str:
        prefix = 'translate to ru: '
        src_text = prefix + input

        input_ids = self.tokenizer(src_text, return_tensors="pt")
        generated_tokens = self.model.generate(**input_ids.to(device))

        result = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        return result


class ImageCaptioner():
    def __init__(self)-> None:
        self.name = "Salesforce/blip-image-captioning-large"
        self.processor = BlipProcessor.from_pretrained(self.name)
        self.model = BlipForConditionalGeneration.from_pretrained(self.name, torch_dtype=torch.float16).to(device)

    def caption(self, image) -> str:
        inputs = self.processor(image, return_tensors="pt").to(device, torch.float16)

        out = self.model.generate(**inputs)
        result = self.processor.decode(out[0], skip_special_tokens=True)
        return result


class Summarizer():
    def __init__(self) -> None:
        self.model_name ='utrobinmv/t5_summary_en_ru_zh_base_2048'
        self.model = T5ForConditionalGeneration.from_pretrained(self.model_name).to(device)
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)

    def summary(self, text: str, lang: str) -> str:
        prefix = 'summary big to ' + lang[:2].lower() + ': '
        src_text = prefix + text
        input_ids = self.tokenizer(src_text, return_tensors="pt")
        generated_tokens = self.model.generate(**input_ids.to(device))

        result = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        return result