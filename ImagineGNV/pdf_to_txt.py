import pdfplumber

text = ""
with pdfplumber.open("ImagineGNV.pdf") as pdf:
    for page in pdf.pages:
        text += page.extract_text() + "\n"

with open("ImagineGNV.txt", "w") as f:
    f.write(text)

