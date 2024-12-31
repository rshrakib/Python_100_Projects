import PyPDF2

def extract_text(file_path):
    with open(file_path, 'rb') as file:
        pdfReader  = PyPDF2.PdfReader(file)
        numPages = len(pdfReader.pages)
        print(f"Total number of pages: {numPages}")
        pageobj = pdfReader.pages[int(input("Enter the pager number: "))  -1]
        text = pageobj.extract_text()
        print(text)

file_path = 'footprinting.pdf'
extract_text(file_path)