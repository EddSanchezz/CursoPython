import requests
from bs4 import BeautifulSoup

url = "https://www.mercadolibre.com.co/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    sections = soup.findAll("li", class_="nav-menu-item")

    section_names = [section.get_text(strip=True) for section in sections if section.get_text(strip=True)]

    print("Secciones:")
    for name in section_names:
        print(name)
else:
    print("Error: ", response.status_code)
