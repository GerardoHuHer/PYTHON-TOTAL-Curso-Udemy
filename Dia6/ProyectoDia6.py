from pathlib import Path

#FUNCIONES GENERALES
def leer_receta(direccion):
    '''
    Esta función toma como parámetro el directorio de un archivo y te devuelve
    la receta leída.
    '''
    receta = Path(direccion)
    print(receta.read_text())

'''
def categoria(opcion_categoria, direccion):
    directorio = Path(direccion / opcion_categoria)
    if directorio in direccion:
        

    #return categ'''




#FUNCIONES PARTICULARES
def informacion(direccion):
    '''
    Esta función nos da información general del recetario, espercíficamente cuántas recertas hay
    '''
    numero_recetas = 0
    print("Las recetas se encuentran en la siguiente dirección: ")
    print(direccion)
    contador_recetas = Path(direccion)
    for txt in Path(contador_recetas).glob('**/*.txt'):
        numero_recetas += 1

    print(f"En total tenemos {numero_recetas}")

def menu(opcion ,direccion):

#def categoria():
    '''
    Esta función "opción 1" del menu, nos va a permitir seleccionar la categoría de comida, ya sea ensalada, carnes etc.
    '''







#MAIN

lista_categorias = []

print("Hola bienvenido, este es un recetario")
informacion('C:\\Users\\huert\\Desktop\\CursoUdePycharm\\Dia6\\Recetas')
