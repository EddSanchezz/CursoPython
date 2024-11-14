from buscador.buscador_funciones import extraer_datos, guardar_cookies, obtener_mejor_producto, agregar_a_whislist
from buscador.opciones_driver import iniciar_chrome
from buscador.utilidades import guardar_articulos_csv

#articulo = obtener_mejor_producto("carro rojo")
#guardar_cookies()
#agregar_a_whislist(articulo)

articulos = extraer_datos("carro rojo")
print(articulos)

#guardar_articulos_csv("rating.csv",articulo)