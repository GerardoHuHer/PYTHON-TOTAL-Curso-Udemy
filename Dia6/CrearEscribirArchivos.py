mi_archivo = open('prueba.txt', 'a') #con r, solo es lectura, con w sobreescribimos el archivo y con a conservamos pero podemos escribir
'''mi_archivo.write('Hola \n')
mi_archivo.write('mundo')'''

'''lista = ['Hola', 'mundo', 'aqui', 'estoy']

for p in lista:
    mi_archivo.writelines(p + '\n')'''

mi_archivo.write('Esta linea no borra el archivo')


mi_archivo.close()