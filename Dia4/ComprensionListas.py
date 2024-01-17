'''palabra = 'Python'

lista = [letra for letra in palabra]
lista1 = [number for number in range(0, 21, 2)]
lista2 = [n/2 for n in range(0, 21, 2)]
lista3 = [n for n in range(0, 21, 2) if n*2 > 10]
lista4 = [n  if n*2 > 10 else 'no' for n in range(0, 21, 2) ]

print(lista)
print(lista1)
print(lista2)
print(lista3)
print(lista4)

'''

pies = [10, 20, 30, 40, 50]
metros = [n*3.281 for n in pies]

print(metros)

