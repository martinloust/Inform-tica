minutos = int(input("Cantidad de minutos: "))
if ((minutos % 60)> 0):
    print(str(int(minutos/60)) + " horas y " + str(minutos % 60) + " minutos")
elif (int(minutos/60) == 1):
    print(str(int(minutos/60)) + " hora")
else: 
    print(str(int(minutos/60)) + " horas")