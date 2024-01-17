'''def suma(**kwargs):
    total = 0 
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total


print(suma(x = 3, y=5, z=2))'''

def prueba(num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    for i in args:
        print(f"arg = {i}")
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
    
arg = [5, 6, 6, 7 , 9]
kwargs = { 'x': 0, 'y': 9}

prueba(15, 50, *arg, **kwargs )


    