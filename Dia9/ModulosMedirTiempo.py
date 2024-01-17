import timeit

declaracion = """
prueba_for(10)
"""

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion, mi_setup, number = 10000000)
print(duracion)

declaracion1 = """
prueba_while(10)
"""

mi_setup1 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion1 = timeit.timeit(declaracion1, mi_setup1, number = 10000000)
print(duracion1)

