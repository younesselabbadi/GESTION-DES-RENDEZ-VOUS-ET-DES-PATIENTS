from PyPDF2 import PdfFileReader, PdfFileWriter
 


def ajouterAuxRapport(chemin,page):
    output = PdfFileWriter()
    pdf = PdfFileReader(open(page, "rb")) 

    if pdf.isEncrypted:
        pdf.decrypt('')

    output.addPage(pdf.getPage(0))  
    outputStream = open("C:\\Users\\Othmane\\Desktop\\test.pdf", "wb")
    output.write(outputStream)
    outputStream.close()