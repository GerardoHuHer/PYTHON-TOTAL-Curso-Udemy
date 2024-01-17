num1 = 90/7
print(f"El número antes de redondear es: {num1}")
#Método para redondar tiene dos parámetros, el primero es el número 
#y el segundo es la cantidad de decimaes que queremos, 
#en caso de no poner segundo parámetro se tomara como 0 , ejemplo:
num1 = round(num1, 2)
print(f"El número redondeado a dos decimales es: {num1}")


print(round(10/3, 2))

valor = 95.6666666666666 
print(round(valor, 2))
print(type(round(valor)))