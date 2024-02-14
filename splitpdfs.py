'''
https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python
'''

from PyPDF2 import PdfWriter, PdfReader

inputpdf = PdfReader(open(r"Test123.pdf", "rb"))

for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    with open(r"test123_pagee%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)