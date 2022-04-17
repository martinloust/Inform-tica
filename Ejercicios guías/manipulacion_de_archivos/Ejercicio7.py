# Escribí un programa que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuántos caracteres tiene.


def palabra_mas_larga(archivo):
    largo = 0
    mas_larga = ""
    with open(archivo, "r") as f:
       palabras = f.read().split()
       for word in palabras:
           if len(word) > largo:
               largo = len(word)
               mas_larga = word
    print("la palabra mas larga es: " + mas_larga + " y tiene " + str(largo) + " caracteres") 

print(palabra_mas_larga("Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"))
       




