import re

def extraer_caracteres_numericos(string):
    lista_numeros = re.findall("[0-9]", string)
    return print("los caracteres númericos son:","".join(lista_numeros))