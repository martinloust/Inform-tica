import re
def extraer_caracteres(string):
    print(re.findall("-(.*?)-", string))