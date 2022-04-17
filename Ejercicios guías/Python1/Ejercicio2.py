string = input("Decime tu apellido: ") 
if  len(string) >= 6:
    print(string.upper()[4:6])
else: 
    print("No tiene la cantidad de letras suficientes")
