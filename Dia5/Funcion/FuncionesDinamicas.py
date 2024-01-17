def chequear3Cifras(lista):
    lista1 = []
    for n in lista:
        if n in range(100, 1000):
            lista1.append(n)
            #return True #El return también saca de la función como el break
        else:
            pass 
    return lista1

lista = [55, 898, 171, 9000]
resultado = chequear3Cifras(lista)
print(resultado)