def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista
    
def promedio(lista):
    prom = sum(lista)/len(lista)
    return prom

    
lista_numeros = [1, 2,3 , 4, 4, 2]

print(reducir_lista(lista_numeros))

