def imprimir(archivo, n):
    with open(archivo, "r") as miarch:
        for line in range(n):
            print(miarch.readline())