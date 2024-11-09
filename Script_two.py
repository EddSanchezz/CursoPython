from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


driver_path = '/path/to/chromedriver'
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.mercadolibre.com.co/"

driver.get(url)

time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')

enlaces = []
for link in soup.find_all('a', href=True):
    enlace = link['href']
    if "mercadolibre.com.co" in enlace:
        enlaces.append(enlace)

driver.quit()


print("Enlaces encontrados en la página:")
for enlace in enlaces:
    print(enlace)
