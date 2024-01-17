def resta_vidas():
    vida = 3
    while True:
        if vida != 0:
            yield f"Te quedan {vida} vidas"
        else:
            yield f"Game Over"
        vida -= 1


perder_vida = resta_vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))


print(1)
print(2)
print(3)
print(4)
print(5)

for i in range(1, 6):
    print(i)