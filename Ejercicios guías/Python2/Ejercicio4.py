peso = int(input("cuantos kg  pesa el paquete? "))
lugar = input("Donde viaja: ")
costo_america_del_sur = 10
costo_america_central = 15
costo_america_del_norte = 18
costo_europa = 24
costo_asia = 30



if peso < 5:
    if lugar == "América del Sur":
        print(peso*costo_america_del_sur)
    if lugar == "América Central":
        print(peso*costo_america_central)
    if lugar == "América del Norte":
        print(peso*costo_america_del_norte)
    if lugar == "Europa":
        print(peso*costo_europa)
    if lugar == "Asia":
        print(peso*costo_asia)
else:
    print("No se puede transportar")