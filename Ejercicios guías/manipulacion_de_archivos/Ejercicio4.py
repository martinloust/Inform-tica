def cantidad_palabras(archivo):
    with open(archivo, "r") as miarch:
        lista_palabras = miarch.read().split()
    print(len(lista_palabras))