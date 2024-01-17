'''La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
1.2.3.4.5.Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
encuentren absolutamente todas las letras es pasar, tanto el texto original como las
letras a buscar, a minúsculas.
Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
para lograr esta parte, recuerda que hay un método de string que permite transformarlo
en una lista y que luego hay una función que permite averiguar el largo de una lista.
Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
claramente echaremos mano de la indexación.
Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
que permita unir esos elementos con espacios intermedios? Piénsalo.
Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
manera de expresarle al usuario tu respuesta.'''

#Ingreso de texto a analizar
text = input('Ingrese el texto a analizar: ')
text = text.lower()

#Separación del texto en una lista
textList = text.split()

#Ingreso de las tres letras que se van a buscar
print('\n')
letras = []
letras.append(input('Ingresa la primera letra: ').lower())
letras.append(input('Ingresa la segunda letra: ').lower())
letras.append(input('Ingresa la tercera letra: ').lower())

#Forma de saber el número de veces que aparece cada una de las letras en todo el texto 
print('\n')
print('CANTIDAD DE LETRAS')
cantLetras1 = text.count(letras[0])
cantLetras2 = text.count(letras[1])
cantLetras3 = text.count(letras[2])

print(f'La letra "{letras[0]}", aparece {cantLetras1} veces')
print(f'La letra "{letras[1]}", aparece {cantLetras2} veces')
print(f'La letra "{letras[2]}", aparece {cantLetras3} veces')

#Cantidad de palabras que tiene el texto
print('\n')
print(f'El texto tiene {len(textList)} palabras')

#Primera y última letra
print('\n')
print(f'La primera letra es : {textList[0][0].upper()}')
print(f'La última letra es : {textList[-1][-1].lower()}')

#Texto invertido
print('\n')
textList.reverse()
textoInv = " ".join(textList)
print(textoInv)

#Revisar si la palabra Python aparece en el texto
print('\n')
print('python' in textList)