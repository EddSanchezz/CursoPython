import requests
from bs4 import BeautifulSoup


def obtener_mejores_productos(palabra):
    url = f"https://www.amazon.com/s?k={palabra.replace(" ","+")}"
    header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"}
    res = requests.get(url,headers=header)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")

        precios = soup.find_all("span", class_="a-price-whole")

        for precio in precios:
            print(precio.get_text(strip=True))

    else:
        print("Error al realizar la solicitud. Código de estado:", res.status_code)
