num1 = 20
num2 = 30.5

num1 = num1 + num2


print(type(num1))
print(type(num2))


print("Conversión explícita")
num3 = 5.8
print(num3)
print(type(num3))

#Forma de cambiar un float a un int
num4 = int(num3)
print(num4)
print(type(num4))

edad = input("Dime tu edad: ")
print(f"Tipo de edad antes de la conversión: {type(edad)}")

edad = int(edad)
new_edad = 1 + edad

print(new_edad)
print(type(new_edad))

print(f"Tu nueva edad: {new_edad}")