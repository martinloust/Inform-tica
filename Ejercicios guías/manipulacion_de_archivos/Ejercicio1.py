from itertools import count

def empiezan_con(letra, archivo):
    with open(archivo, "r") as miarch:
        count = 0
        for line in miarch:
            if line[0] != letra.upper or line [0]:
                count += 1
        print("el numero de lineas que no empiezan con " + letra + " es " + str(count))