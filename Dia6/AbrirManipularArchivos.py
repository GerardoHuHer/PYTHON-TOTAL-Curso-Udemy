mi_archivo = open('prueba.txt')

'''print(mi_archivo.read())


una_linea = mi_archivo.readline()
print(una_linea.strip()) #Esta método sirve para eliminar el enter entre las líneas

una_linea = mi_archivo.readline()
print(una_linea.upper())'''

'''for l in mi_archivo:
    print('Aquí dice: ' + l )'''

todas = mi_archivo.readlines() #Este método transforma el texto en una lista

todas = todas.pop()

print(todas)


mi_archivo.close()
