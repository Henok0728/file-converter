from fpdf import FPDF
from pypdf import PdfMerger as pdfmerger
from pdf2docx import converter
from PIL import Image
from docx2pdf import convert

def img_to_pdf():
    print("image to pdf converter made by MR Henok Gizaw")
    print("----------------------------------------------")
    img_path= input(" enter the path of the image: ")
    output_pdf = input("name your file name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.image(img_path, x=0 , y=0, w=210,h=297 )
    pdf.output(output_pdf)
    print(f" saved image as {output_pdf} " )
def mergepdf():
    merger = pdfmerger()
    while True:
        pdf = input("enter the path of pdf file: ")
        if pdf == "":
            break
        merger.append(pdf)
    merger.write("Milestone02_Henok_Gizaw_25.05.2025.pdf")
    merger.close()
def pdf_to_word():
    pdf= input("enter the pdf file: ")
    doc = "assignment.docx"
    cv = converter(pdf)
    cv.convert(doc)
    cv.close()
    print("operation completed")
def word_to_pdf():
    convert("input.docx", "output.pdf")
    print("file is successfully converted")

