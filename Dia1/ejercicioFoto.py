'''
Realice un código que solicite los valores de las variables M y N donde M > N.
Luego presente en pantalla el resultado de la siguiente serie

1/M + 1/(M+1) + 1/(M+2) + ... + 1/(M+N)
'''
acum = 0 
while True:
    m = int(input("Ingrese el número M: "))
    n = int(input("Ingrese el número N: "))
    if(n > m):
        break
    elif n <= m : 
        print("Recuerde que N tiene que ser mayor que M")
for i in range(0, n):
    num = 1/(m + i)
    acum += num 
print(acum)