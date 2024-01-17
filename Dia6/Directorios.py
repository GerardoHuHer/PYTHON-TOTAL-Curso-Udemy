import os
#ruta = os.getcwd() #Sirve para obtener la ruta
#ruta = os.chdir('C:\\Users\\huert\\OneDrive\\Escritorio\\alternativo') #Así cambiamos de directorio
#archivo = open('pruebaalternativa.txt')
#ruta = os.makedirs('C:\\Users\\huert\\OneDrive\\Escritorio\\alternativo\\otra') #Creamos un nuevo una nueva carpeta
#os.rmdir('C:\\Users\\huert\\OneDrive\\Escritorio\\alternativo\\otra.txt') #Elimina carpeta

'''otro_archivo = open('C:\\Users\\huert\\OneDrive\\Escritorio\\alternativo\\pruebaalternativa.txt')
print(otro_archivo.read())

otro_archivo.close()
'''

from pathlib import Path
carpeta = Path('C:/Users/huert/OneDrive/Escritorio/alternativo')
archivo = carpeta / 'pruebaalternativa.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

mi_archivo.close()
