class Pajaro:

    alas = True

    #Constructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    #Métodos de instancia porque afectan al self, o sea a cada instancia que creemos, estos pueden acceder a los atributos y modificarlos

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    def piar(self):
        print('Pio mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pájaro ha volado {metros} metros')
        self.piar()

    #Métodos de clase
    @classmethod #Decorador
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(cls.alas)

    #Métodos estáticos
    @staticmethod
    def mirar():
        print('El pájara mira')






Pajaro.poner_huevos(3)
#No puedes llamar métodos de instancia si no has instanciado la clase

Pajaro.mirar()

'''piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(100)

piolin.pintar_negro()

piolin.alas = False
piolin.alas'''