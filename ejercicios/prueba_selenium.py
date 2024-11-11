from selenium.webdriver.common.by import By
import time
from buscador.opciones_chrome import iniciar_chrome

driver = iniciar_chrome()
palabra = "carros rojos"
url = f"https://www.amazon.com/s?k={palabra.replace(' ', '+')}"
driver.get(url)

time.sleep(3)

driver.quit()
