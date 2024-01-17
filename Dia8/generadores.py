"""def mi_funcion():
    lista = []
    for i in range(1, 5):
        lista.append(i * 10)
    return lista


def mi_generador():
    for j in range(1, 5):
        yield j * 10


print(mi_funcion())
#print(next(mi_generador()))

g = mi_generador()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
"""

def mi_generador():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x


g = mi_generador()

print(next(g))
print(next(mi_generador()))
print(next(g))
print("Hola mundo")
for i in "Hola mundo":
    print(i)
print(next(g))
print(next(g))


"""def mi_generador():
    x = 0
    while True:
        yield x
        x += 1


generador = mi_generador()

print(next(generador))"""
