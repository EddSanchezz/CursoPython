def agregar_articulos_txt(texto):
    with open("recursos/rating.txt", "a", encoding="utf-8") as txt:
        if isinstance(texto, dict):
            for k, v in texto.items():
                agregar_articulos_txt(f"{k}:{v}")
        else:
            txt.write(texto + "\n")

def cambiar_articulos_txt(texto):
    with open("recursos/rating.txt", "w", encoding="utf-8") as txt:
        txt.write(texto)

def leer_articulos_txt():
    with open("recursos/rating.txt", "r", encoding="utf-8") as txt:
        return txt.read()


