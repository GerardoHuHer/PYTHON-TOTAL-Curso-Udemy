def suma():
    n1 = int(input("Ingrese un número 1: "))
    n2 = int(input("Ingrese un número 2: "))
    print(n1 + n2)
    print("Gracias por sumar" + n1)


def pedir_numero():
    while True:
        try:
            num = int(input("Dame un número: "))
        except:
            print("Ese no es un número")
        else:
            print(f"Ingresaste el número {num}")
            break
    print("Gracias")


pedir_numero()
'''try:
    suma()
except TypeError:
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un número")'''

'''try:
    #Código que se quiere probar
    suma()
except:
    #Código a ejecutar si hay un error
    print("Error algo no ha salido bien")
else:
    #Código a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    #Código que se va a ejecutar de todos modos
    print("Eso fue todo")'''

