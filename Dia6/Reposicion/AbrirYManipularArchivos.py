mi_archivo = open("MiArchivo.txt")


# Forma de leer el archivo.
# todo_el_archivo = mi_archivo.read()

# Forma de leer una sola línea
# una_linea = mi_archivo.readline()

# Forma de iterar con las lineas de un archivo.
"""
for l in mi_archivo:
    print(f"Aquí dice: {l}")
"""

# Ocupamos readlines para guardar todas las lineas en una lista
lista_todas = mi_archivo.readlines()
print(lista_todas)
mi_archivo.close()
