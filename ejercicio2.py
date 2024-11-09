import requests
from bs4 import BeautifulSoup

url = "https://techpulser.wordpress.com/"
headers = {"user-agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text,"html.parser")