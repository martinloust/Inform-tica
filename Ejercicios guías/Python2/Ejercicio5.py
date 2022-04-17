numero_ingresado = int(input("Ingrese un numero"))
if 1 <= numero_ingresado <= 7:
    if numero_ingresado == 1:
        print("Lunes")
    if numero_ingresado == 2:
        print("Martes")
    if numero_ingresado == 3:
        print("Miercoles")
    if numero_ingresado == 4:
        print("Jueves")
    if numero_ingresado == 5:
        print("Viernes")
else:
    print("El numero es incorrecto")