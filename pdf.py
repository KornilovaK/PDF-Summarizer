import fitz
from PyPDF2 import PdfReader
from io import BytesIO
from PIL import Image
from ml import Translator, ImageCaptioner, Summarizer


class Reader():
    def __init__(self, path: str) -> None:
        self.doc = fitz.open(path)
        self.reader = PdfReader(path)
        self.text, self.links = '', []
        self.pages_count = self.doc.page_count
        self.captioner = ImageCaptioner()
        self.translator = Translator()
        self.summarizer = Summarizer()

    def get_image(self, image_num: int):
        img_dictionary = self.doc.extract_image(image_num)
        img_extension = img_dictionary["ext"]
        img_binary = img_dictionary["image"]
        image_io = BytesIO(img_binary)
        image = Image.open(image_io)

        return image

    def convert(self, lang: str) -> list:
        for page_num in range(self.pages_count):
            page = self.doc.load_page(page_num)
            page_txt = self.reader.pages[page_num]
            text_page = page_txt.extract_text()
            
            page_links = page.get_links()
            images = page.get_images()

            if len(page_links) != 0:
                self.links.extend(page_links)

            if len(images) != 0:
                for image in images:
                    img = self.get_image(image[0])
                    caption = self.captioner.caption(img)
                    if lang == 'Russian':
                        caption = self.translator.translate(caption)
                    text_page += caption
                        
            self.text += self.summarizer.summarize(text_pages, lang)
        return [self.text, self.links]