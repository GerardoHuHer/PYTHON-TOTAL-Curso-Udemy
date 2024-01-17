from random import *

aleatorio = randint(1, 50) #Genera un número aleatorio en el rango seleccionado 
print(aleatorio)

uniforme = round(uniform(1, 5), 2) #Nos va a dar un valor decimal 
print(uniforme)

randome = random() #Genera un decimal entre 0 y 1
print(randome)

colores = ['verde', 'rojo', 'azul', 'amarillo']
coice = choice(colores) #Elemento aleatorio en una lista
print(coice)

numeros = list(range(5, 50, 5))
print(numeros)
shuffle(numeros) #Sirve para mezclar coleccionables, mutables y al igual que sort modifica la lista entonces no se puede almacenar en otra lista
print(numeros)



