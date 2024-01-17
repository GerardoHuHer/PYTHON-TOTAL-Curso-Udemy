def devolver_distintos(num1, num2, num3 ):
    lista = [num1, num2, num3]
    if (num1 + num2 + num3) > 15:
        print(max(lista))
    elif (num1 + num2 + num3) < 10:
        print(min(lista))
    elif 10 < (num1 + num2 + num3) < 15:
        lista.sort()
        print(lista[1])

devolver_distintos(6, 3,2 )