# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un documento ya existente.

def guardar_contenido(arch1, arch2, arch_existente):
    with open(arch1, "r") as f1, open(arch2, "r") as f2, open(arch_existente, "a") as f3:
        for l1, l2 in zip(f1, f2):
            f3.write(l1)
            f3.write("/n")
            f3.write(l2)
        

    

