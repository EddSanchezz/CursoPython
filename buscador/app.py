from buscador.buscador_funciones import extraer_datos


def main():
    nombre_articulo = "carros rojos"
    # buscar los artículos relacionados a una palabra y los guarda con su respectivo nombre y precio
    extraer_datos(nombre_articulo)