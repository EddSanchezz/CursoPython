from selenium.webdriver.common.by import By
import time
from buscador.opciones_driver import iniciar_chrome
import json
from config_amazon import *
from buscador.utilidades import guardar_articulo_csv
from buscador.utilidades import leer_articulos_csv


driver = iniciar_chrome()

def extraer_datos(nombre_articulo: str) -> list:
    url = f"https://www.amazon.com/s?k={nombre_articulo.replace(' ', '+')}"
    driver.get(url)
    time.sleep(2)

    div = driver.find_elements(By.CSS_SELECTOR, "div.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small")
    time.sleep(2)


    articulos = []
    for art in div:
        nombres_art = art.find_elements(By.CSS_SELECTOR,"span.a-size-base-plus.a-color-base.a-text-normal")
        precios_entero = art.find_elements(By.CSS_SELECTOR,"span.a-price-whole")
        precios_fraccion = art.find_elements(By.CSS_SELECTOR,"span.a-price-fraction")
        calificaciones = art.find_elements(By.CSS_SELECTOR, "span.a-icon-alt")
        cant_calificaciones = art.find_elements(By.CSS_SELECTOR, "span.a-size-base.s-underline-text")

        for i in range(len(nombres_art)):
            nombre = nombres_art[i].text if i < len(nombres_art) else "No disponible"
            precio = precios_entero[i].text + "." + precios_fraccion[i].text if i < len(precios_entero) and i < len(precios_fraccion) else "No disponible"
            calificacion = calificaciones[i].get_attribute("innerText") if i < len(calificaciones) else "No disponible"
            cantidad = cant_calificaciones[i].text if i < len(cant_calificaciones) else "No disponible"

            articulos.append([nombre,precio, calificacion[0:3],cantidad.replace(",","")])

    driver.quit()
    return articulos


def obtener_mejor_producto(palabra):
    lista_productos = extraer_datos(palabra)
    mejor_producto = None
    niveles_calificacion = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

    for nivel in niveles_calificacion:
        for producto in lista_productos:
            nombre, precio, calificacion, cantidad_calificaciones = producto
            calificacion = float(calificacion)
            cantidad_calificaciones = int(cantidad_calificaciones) if cantidad_calificaciones else 0

            if calificacion >= nivel:
                if (mejor_producto is None or
                        cantidad_calificaciones > mejor_producto[3] or
                        (cantidad_calificaciones == mejor_producto[3] and calificacion > mejor_producto[2])):
                    mejor_producto = [nombre, precio, calificacion, cantidad_calificaciones]

        if mejor_producto:
            break

    return mejor_producto


def login_amazon():
    print("Login en amazon desde cero")
    driver.get("https://es.pornhub.com/")
    aceptar = driver.findelement("")
    input("pulsa ENTER para salir")
    driver.quit()

