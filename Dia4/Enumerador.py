lista = ['a', 'b', 'c']
indice = 0
for i in lista:
    print(indice, i)
    indice += 1 

lista1 = ['a', 'b', 'v']
for j, i in enumerate(lista1):
    print(j, i)

listTuples = list(enumerate(lista))
print(listTuples)
print(listTuples[1][1])

#EjercicioImprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:

'''lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:

Loops

Condicionales if

El método enumerate()

Métodos de strings o indexado'''

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for i in lista_nombres:
    if i.startswith("M"):
        print(lista_nombres.index(i))

