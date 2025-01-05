# for each HW 1-8, download file https://2prime.github.io/files/IEMS402/IEMS_402_Homework1.pdf to the folder

import requests

for i in range(1, 9):
    url = f"https://2prime.github.io/files/IEMS402/IEMS_402_Homework{i}.pdf"
    response = requests.get(url)
    with open(f"HW{i}/HW{i}_assignment.pdf", "wb") as f:
        f.write(response.content)
    print(f"Downloaded HW{i}.pdf")