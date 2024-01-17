"""dictionary= {'c1': 'valor1', 'c2': 'valor2', 'c3': 'valor3'}
print(dictionary)

resultado = dictionary['c1']
print(resultado)"""

#Como consultar una clave en específico de un diccionario

"""
cliente = {'nombre': 'Juan',
 'apellido': 'Fuentes',
  'peso': 80,
   'estatura': '1.76'}

consulta = cliente['apellido']
print(consulta)"""

#Como consultar listas o diccionarios anidados

"""dic = {'c1': 55, 
'c2': [1, 2, 3,],
'c3': {'s1': 100, 's2':200}}

print(dic['c2'][1]) #Imprime lo que sea que haya en el diccionario en la clave 2 "c2" en el índice 1

print(dic['c3']['s1']) #Imprime lo que sea que haya en el diccionario en la clave 2 "c2" en la clave s1"""

#Forma de acceder a elementos de un diccionario y aplicarle métodos

"""dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic['c1'][0].upper())"""

#Forma de añadir elementos a un diccionario

dic = {1: 'a', 2: 'b'}
print(dic)

dic[3] = 'c' #Forma de añadir elementos a un diccionario
print(dic)

#Forma de sobreescribir elementos
dic[2] = 'B'
print(dic)

#Forma de conocer todas las claves
print(dic.keys())

#Forma de conocer los valores
print(dic.values())

#Forma de conoocer todos los elementos de un diccionario
print(dic.items())



