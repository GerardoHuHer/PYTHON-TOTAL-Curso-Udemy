"""def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    else:
        return minuscula


def una_funcion(funcion):
    return funcion


mi_funcion = mayuscula

mi_funcion("python")

una_funcion(mayuscula("probando"))


operacion = cambiar_letras("may")

operacion("palabra")
"""


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")

    return otra_funcion



def mayusculas(texto):
    print(texto.upper())



def minuscula(texto):
    print(texto.lower())

mayusculas("Python")


mayuscula_decorada = decorar_saludo(mayusculas)

mayuscula_decorada("gerardo")

