def guardar_lineas(archivo, n):
    archivo_lineas = []
    with open(archivo, "r") as miarch:
        archivo_lineas.append(miarch.readline())
    print(archivo_lineas[-n:])