from random import randint

#Saluda inicial y petición de nombre
player = input('Hola bienvenido, por favor introduce tu nombre: ')
print(f'Bueno, {player}, tienes 8 intentos para tratar de adivinar un número entre 1 y 100, recuerda que tus errores contarán como intento')
n = 8

#Generador de número aleatorio
randNum = randint(1, 101)

#Acumulador del número de turnos
acumTur = 0

#Bucle con todo el juego
while n > 0:
    print(f'Tienes {n} turnos')

    #Petición del número del usuario 
    number = int(input("Introduce tu número: "))

    #Suma al número de turnos
    acumTur += 1

    #Caso en que el judador gana
    if number == randNum:
        print(f'Felicidades {player} has ganado, el número que pensé era {randNum}, solo te ha tomado {acumTur} turnos ')
        break
    
    #Caso que el jugador introduce un número que no está en el rango
    elif (number < 0) or (number > 100):
        print('Ups, este error te acaba de costar un turno, recuerda que solo puede estar entre 1 y 100')

    #Caso en que el número introducido es menor
    elif number < randNum:
        print('El número que dices es menor al número que pienso')

    #Caso en que el número introducido es mayor
    elif number > randNum:
        print('El número que dices es mayor al número que pienso')

    #Descontador de turnos
    n -= 1

#Mensaje final en caso de perder
if n == 0:
    print(f'Lo siento el número que pensaba era {randNum}')

#Mensaje final en caso de haber ganado
else:
    print(f'Has adivinado mi número, felicidades')