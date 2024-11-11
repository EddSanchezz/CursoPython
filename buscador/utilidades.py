def cambiar_articulos_txt(texto):
    with open("rating.txt","a", encoding = "utf-8") as txt:
        txt.write(texto)
    
def agregar_articulos_txt(texto):
    with open("rating.txt","w", encoding = "utf-8") as txt:
        txt.write(texto)
