def palabra(word):
    lista = []
    for i in word:
        lista.append(i)
    lista = list(set(lista))
    lista.sort()
    print(lista)

palabra('arboleda')