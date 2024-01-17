class Pajaro:
    alas = True #Atributo de clase porque todos los pájaros tienen alas

    def __init__(self, color, especie): #Constructor de la clase Pajaro, estos son atributos de instancia
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro('negro', 'tucan')

print(f"Mi pájaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

print(Pajaro.alas)
print(mi_pajaro.alas)