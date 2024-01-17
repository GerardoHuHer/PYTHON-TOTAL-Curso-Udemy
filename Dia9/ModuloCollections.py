from collections import namedtuple

Persona = namedtuple('Persona', ["nombre", "altura", "peso"])
ariel = Persona("Ariel", 1.76, 79)

print(ariel.nombre)
print(ariel.altura)
print(ariel.peso)

