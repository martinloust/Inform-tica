import re
def remplazar_espacios_tab(string):
    print(re.sub("[\s\t]", ";", string))