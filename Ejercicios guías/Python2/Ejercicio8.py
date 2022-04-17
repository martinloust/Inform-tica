lista1 = []
lista2 = []
lista3 =[]
for x in range(5):
    valor = int(input("Ingrese un valor entero: "))
    lista1.append(valor)
for x in range(5):
    valor2 = int(input("Ingrese un valor entero: "))
    lista2.append(valor2)
for x in range(len(lista1)):
    lista3.append(lista1[x]+lista2[x])

print(lista3)