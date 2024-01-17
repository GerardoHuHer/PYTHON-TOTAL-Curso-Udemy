"""miSet = set([1, 2, 3, 4, 5, 1, 1, 2, (1,2,3)]) #Elimina todos los elementos repetidos, sí admite tuples ya que un 
#set requiere que sus elementos sean inmutables y las listas y los diccionarios no lo son pero los tuples sí
print(miSet)

otroSet = {1, 2, 3}
print(otroSet)

print(len(miSet))
print(2 in miSet)"""


'''s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)'''

#Métodos de sets

s1 = {1, 2, 3}

s1.add(4)
print(s1)

s1.remove(3)
print(s1)

s1.discard(6) #Funciona igual que remove pero en caso de no estar el elemento no marcará error como remove
print(s1)

s1.pop() #Como en los sets no hay orden entonces no puede eliminar el último elemento sino que eliminará uno aleatorio 
print(s1)

s1.clear()
print(s1)
