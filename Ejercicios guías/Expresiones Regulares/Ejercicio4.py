# Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).
import re

def que_tenga_guion(string):
    return print((re.search("(\w*)[_](\w*)")), string)


