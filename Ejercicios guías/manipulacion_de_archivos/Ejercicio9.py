# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

def word_counter(archivo):
        frecuencias = dict()
        with open(archivo, "r") as f:
            word_list = f.read().split()
            for i in word_list:
                if i in frecuencias:
                    frecuencias[i] += 1
                else:
                    frecuencias[i] = 1
            for word in frecuencias.keys():
                frecuencias[word] = round(frecuencias[word] / len(word_list),3)
        print(frecuencias)



