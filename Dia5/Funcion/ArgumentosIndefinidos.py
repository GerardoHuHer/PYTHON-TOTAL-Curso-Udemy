def suma(*args):
    total = 0 
    for i in args:
        total += i
    return total

    #Otra forma de hacer es return sum(args)


print(suma(5,6, 5, 6,6 ,7, 7,8, 8, 899, 6 ))