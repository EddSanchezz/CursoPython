from buscador.driver_indetectable import login_google
from buscador_funciones import guardar_cookies_url

#print(extraer_datos("botellas de vidrio"))

#articulo = obtener_mejor_producto("carro rojo")
#agregar_a_whislist(articulo)
#guardar_articulos_csv("rating.csv",articulo)

#guardar_cookies_amazon()

#driver = iniciar_webdriver_indetectable()
driver = login_google()
guardar_cookies_url(driver,"cookies_google")


