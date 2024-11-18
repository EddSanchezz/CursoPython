import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from driver_indetectable import login_google
from opciones_driver import iniciar_firefox
from Config import *
from config import *


def extraer_datos(nombre_articulo: str) -> list[list]:
    driver = iniciar_firefox()
    url = f"https://www.amazon.com/s?k={nombre_articulo.replace(' ', '+')}"
    driver.get(url)
    time.sleep(2)

    div = driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div/div/div/span/div")
    time.sleep(2)

    articulos = []
    for art in div:
        nombres_art = art.find_elements(By.CSS_SELECTOR, "span.a-size-base-plus.a-color-base.a-text-normal")
        precios_entero = art.find_elements(By.CSS_SELECTOR, "span.a-price-whole")
        precios_fraccion = art.find_elements(By.CSS_SELECTOR, "span.a-price-fraction")
        calificaciones = art.find_elements(By.CSS_SELECTOR, "span.a-icon-alt")
        cant_calificaciones = art.find_elements(By.CSS_SELECTOR, "span.a-size-base.s-underline-text")
        enlaces = art.find_elements(By.CSS_SELECTOR, "a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")

        for i in range(len(nombres_art)):
            nombre = nombres_art[i].text if i < len(nombres_art) else "No disponible"
            precio = f"{precios_entero[i].text}.{precios_fraccion[i].text}" if i < len(precios_entero) and i < len(precios_fraccion) else "No disponible"
            calificacion = calificaciones[i].get_attribute("innerText")[:3] if i < len(calificaciones) else "No disponible"
            cantidad = cant_calificaciones[i].text.replace(",", "") if i < len(cant_calificaciones) else "No disponible"
            enlace = enlaces[i].get_attribute("href") if i < len(enlaces) else "No disponible"

            articulos.append([nombre, precio, calificacion, cantidad, enlace])

    driver.quit()
    return articulos


def obtener_mejor_producto(palabra: str) -> list:
    lista_articulos = extraer_datos(palabra)

    lista_articulos_filtrada = [
        articulo for articulo in lista_articulos
        if articulo[3].isdigit() and articulo[2].replace('.', '', 1).isdigit()
    ]

    mejor = max(lista_articulos_filtrada, key=lambda x: (int(x[3]), float(x[2])))
    return mejor


def guardar_cookies(driver):
    driver = iniciar_firefox()
    print("Login en amazon desde cero")
    driver.get("https://www.amazon.com")

    input("Presiona Enter después de iniciar sesión en la pestaña...")
    with open("buscador/cookies_amazon.json", "w") as file:
        for cookie in driver.get_cookies():
            json.dump(cookie, file)


def guardar_cookies_url(driver, nombre_archivo):
    input("Presiona Enter después de iniciar sesión en la pestaña...")
    with open(f"buscador/{nombre_archivo}.json", "w") as file:
        for cookie in driver.get_cookies():
            json.dump(cookie, file)
    driver.quit()


guardar_cookies_url(driver=login_google(), nombre_archivo="cookies_google")


def login_amazon():
    driver = iniciar_firefox()
    with open("cookies_amazon.json", "r") as file:
        cookies = json.load(file)

    driver.get("https://www.amazon.com/robots.txt")
    for cookie in cookies:
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)

    driver.refresh()
    return driver


def agregar_a_whislist(articulo: list):
    driver = login_amazon()
    driver.get(articulo[4])

    boton_lista_deseos = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[contains(@title,'Agregar a la Lista')]"))
    )
    boton_lista_deseos.click()
    print("Producto agregado a la lista de deseos.")
    driver.quit()
