def num0(*args):
    contador = 0
    for i in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1]:
            return True
        else:
            contador += 1
    return False


resultado = num0(5, 6, 7, 8, 0, 0, 5, 4)
print(resultado)