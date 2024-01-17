'''
class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')



class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color) #Es lo mismo que escribir lo que está abajo
        #self.edad = edad
        #self.color = color
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('Pio')

    def volar(self, metros):
        print(f'El pájaro vuela {metros}')


piolin = Pajaro(2, 'amarillo', 60)
mi_animal = Animal(5, 'negro')

piolin.hablar()
piolin.volar(100)
'''

class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('jajaja')

    def hablar(self):
        print('¿Qué tal?')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()

mi_nieto.hablar() #En este caso donde dos métodos de los que hereda llevan el mismo nombre,
# va a decir el hablar de padre ya que de él heredo primero
mi_nieto.reir()

print(Nieto.__mro__)