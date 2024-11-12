from selenium.webdriver.common.by import By
import time
from buscador.opciones_driver import iniciar_chrome
from buscador.utilidades import agregar_articulos_txt


def extraer_datos(nombre_articulo: str) -> dict:
    driver = iniciar_chrome()
    palabra = nombre_articulo
    url = f"https://www.amazon.com/s?k={palabra.replace(' ', '+')}"
    driver.get(url)

    div = driver.find_elements(By.CSS_SELECTOR, "div.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small")
    time.sleep(3)


    articulos = {}
    for art in div:
        calificaciones = art.find_elements(By.CSS_SELECTOR, "span.a-icon-alt")
        nombres_art = art.find_elements(By.CSS_SELECTOR,"span.a-size-base-plus.a-color-base.a-text-normal")
        precios_entero = art.find_elements(By.CSS_SELECTOR,"span.a-price-whole")
        precios_fraccion = art.find_elements(By.CSS_SELECTOR,"span.a-price-fraction")

        for i in range(len(precios_entero)):
            nombre = nombres_art[i].text
            precio = [precios_entero[i].text + "." + precios_fraccion[i].text,]
            articulos[nombre] = precio

    print(articulos)

    driver.quit()

def guardar_articulos_txt(articulos: dict):
    for llave, valor in articulos.items():
        agregar_articulos_txt(f"{llave}: {valor}")


extraer_datos("carros rojos")