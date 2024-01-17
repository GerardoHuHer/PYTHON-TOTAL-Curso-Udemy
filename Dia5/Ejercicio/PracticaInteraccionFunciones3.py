from random import choice

def lanzar_moneda():
    lista = ['Cara', 'Cruz']
    suerte = choice(lista)
    return suerte

def probar_suerte(resultado, lista):
    if resultado == 'Cara':
        print('La lista se autodestruirá')
        lista.clear()
        return lista
    else:
        print('La lista fue salvada')
        return lista



lista_numeros = [1, 2, 3,4,4, 5,5, 6]

resultado = lanzar_moneda()

probar_suerte(resultado, lista_numeros)

