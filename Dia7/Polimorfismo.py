class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'{self.nombre} dice muuuu')

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'{self.nombre} dice beee')

vaca1 = Vaca('Vaca')
oveja1 = Oveja('Ove')

animales = [vaca1, oveja1]

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
