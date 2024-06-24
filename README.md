# PDF-Summarizer
<img src="pdf-icon.png" alt="pdf-icon" width="300" height="300">


This is my little project for the interview from MTC
It is a web app, that can summarize pdf lectures in both English and Russian. The program will go through your file, collecting text, links (which can be placed), and if there is an image in it, the application will caption it. Summarizing takes place on each page

Understand the limitations: don't send files with the chemical reactions or mathematical formulas to it,  it'll return you not quite accurate data.

Although I use open source decisions from Hugging Face, I provide notebooks to fine-tune the models for the relevant tasks (to learn more, visit **notebooks**).

PDF-Summarizer is using gpu -> Cuda, however to run the app on the cpu, you can run models with the ONNX runtime