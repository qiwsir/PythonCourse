#coding:utf-8
'''
the example for converting image to pdf
install img2pdf: pip3 install img2pdf
filename: convertimgtopdf.py
'''

import os
import img2pdf

with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert(["./imgs/" + i for i in os.listdir('./imgs') if i.endswith(".png")]))