# for each HW 1-8, download file https://2prime.github.io/files/IEMS402/IEMS_402_Homework1.pdf to the folder

import requests

for i in range(1, 9):
    url = f"https://2prime.github.io/files/IEMS402/IEMS_402_Homework{i}.pdf"
    response = requests.get(url)
    with open(f"HW{i}/HW{i}_assignment.pdf", "wb") as f:
        f.write(response.content)
    print(f"Downloaded HW{i}.pdf")


# make a concatenated PDF file: HW{x}/HW{x}.pdf for x in 1 to 8, into PDF named "HWs.pdf"
import PyPDF2

pdf_writer = PyPDF2.PdfWriter()
for i in range(1, 9):
    with open(f"HW{i}/HW{i}.pdf", "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

# Save the concatenated PDF to a HWs.pdf 

with open("HWs.pdf", "wb") as output_pdf:
    pdf_writer.write(output_pdf)
    



