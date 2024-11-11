import requests
from bs4 import BeautifulSoup


url = "https://techpulser.wordpress.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    print("titulo: ", soup.title.text)
    print(soup.findAll())
    
    enlaces = soup.find_all("a")
    print("enlaces: ")
    for enlace in enlaces:
        print(enlace.get("href"))
else:
    print("Error")
