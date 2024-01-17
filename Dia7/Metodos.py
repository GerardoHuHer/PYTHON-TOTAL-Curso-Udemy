class Pajaro:

    alas = True

    #Constructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    #Métodos

    def piar(self):
        print('Pio mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pájaro ha volado {metros} metros')



piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(100)