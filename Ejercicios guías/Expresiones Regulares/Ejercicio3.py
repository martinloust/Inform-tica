import re
def de_pe_a_pa(string):
    return bool((re.search(("h(e*)", "(he+)\b"), string)))