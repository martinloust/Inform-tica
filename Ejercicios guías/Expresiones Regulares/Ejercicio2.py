import re
def caracteres_permitidos(string):
    return bool((re.search("[\w]", string))) is None