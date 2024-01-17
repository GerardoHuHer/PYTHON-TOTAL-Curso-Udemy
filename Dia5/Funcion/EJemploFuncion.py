def cafeMasCaro(listaPrecios):
    '''
    Con esta función obtenemos cual es el cafe más caro recorriendo la lista de tuples
    '''
    precioMayor = 0
    cafeCaro = ''

    for cafe, precio in listaPrecios:
        if precio > precioMayor:
            precioMayor = precio
            cafeCaro = cafe
        else:
            pass

    return (cafeCaro, precioMayor)


preciosCafe = [('capuchino', 1.5), ('Expresso', 2.5), ('Moka', 1.9)]
print(cafeMasCaro(preciosCafe))