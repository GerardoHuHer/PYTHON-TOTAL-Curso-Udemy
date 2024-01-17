'''
Métodos a ver:
upper() - pasa a mayúsculas 
lower() - pasa a minúsculas
split() - separalo en partes(lista)
join() - unir items usando separador
find() - encontrar un sub-string
replace() remplazar un sub-string
'''

texto = "Este es el texto de Federico"

#resultado = texto.upper()
#resultado = texto[2].upper() #Con esto le decimos que solo la letra en el índice 2 va a hacerce mayúscula
#resultado = texto.lower() #Lo mismo que upper() pero para minúsculas
#resultado = texto.split() #Este método almacena cada palabra por separado en una lista
#resultado = texto.split("t") #Este método almacena cada palabra por separado en una lista en este caso lo separa respecto a la letra t
#resultado = texto.split()
#print(resultado)

'''
a = "aprender"
b = "Python"
c = "es"
d =  "genial"
e = " ".join([a, b, c, d])
print(e)
'''

#resultado = texto.find("") #Este método no marca error en caso de no encontrar el string buscado

resultado = texto.replace("Federico", "Gerardo")

print(resultado)

'''texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(texto)
resultado = texto.replace("difícil", "fácil")
resultado1 = resultado.replace("mala","buena")
print(resultado1)'''




