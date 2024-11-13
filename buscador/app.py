from buscador.buscador_funciones import extraer_datos, guardar_cookies, obtener_mejor_producto, agregar_a_whislist
from buscador.opciones_driver import iniciar_chrome


articulo = obtener_mejor_producto("carro rosa")
#guardar_cookies()
agregar_a_whislist(articulo)

