from random import *
# Lista inicial
palitos = ['-', '--', '---', '----']

#Función encargada de mezclar los palitos
def mezclarPalitos (lista):
    shuffle(lista)
    return lista

#Función para pedir el intento 
def probarSuerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')
    
    return int(intento)

#Función para comprobar el intento 
def revisarIntento(lista, intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos')
    else: 
        print('Esta vez te has salvado')

    print(f'Te ha tocado {lista[intento - 1]}')


#Main____________________________________________________________________________________________________

palitosMezclados = mezclarPalitos(palitos)
seleccion = probarSuerte()

revisarIntento(palitosMezclados, seleccion)