'''lista = ['a', 'b', 'c', 'd', 'e']

for i in lista:
    numeroLetra = lista.index(i) + 1
    print(f'Letra {numeroLetra}: {i}')'''

'''lista = ['Gerardo', 'Carlos', 'Alejandro', 'Lilia', 'Arnulfo']

for name in lista:
    if name.startswith('A'): #Con este método podemos ver con que letra empieza un string
        print(name)
    else: 
        print(f'El nombre {name} no comienza con la letra A')'''

'''number = [1, 2, 3, 4, 5]
miValor = 0
for i in number:
    miValor = miValor + i
print(miValor)'''

'''palabra = 'python'

for i in palabra:
    print(i)'''
"""
for a,b in [[1, 2], [3, 4], [5,6]]:
    print(a)
    print(b)"""

dic = {'c1': 'a', 'c2': 'b', 'c3': 'c'}

for i, j in dic.items():
    print(i)
    print(j)
