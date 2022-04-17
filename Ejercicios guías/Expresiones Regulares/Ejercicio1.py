import re
def caracteres_permitidos (string):
    return bool((re.search("[a-zA-Z0-9]", string)))