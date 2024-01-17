# CLASES
class Persona:
    # Constructor, de persona
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    # Constructor, de cliente que hereda de Persona
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    # Definición de método especial str
    def __str__(self):
        return f'El número de cuenta de {self.nombre}{self.apellido} es: {self.numero_cuenta} y el Balance: {self.balance} '

    def depositar(self):

        deposito = int(input('Ingrese la cantidad de dinero que desea depositar: '))
        if deposito < 0:
            print('No puede depositar cantidades negativas')
        else:
            self.balance += deposito
            return self.balance

    def retirar(self):
        retiro = int(input('Ingrese la cantidad de dinero que desea retirar: '))
        if (retiro > self.balance) or (retiro < 0):
            print('No puede realizar el retiro porque no tiene tal cantidad de dinero')
        else:
            print(f'Ha retirado ${retiro}, su saldo actual es de {self.balance - retiro}')
            self.balance = self.balance - retiro
            return self.balance


#FUNCIONES
def instanciarCliente():
    name = input('Ingrese su nombre: ')
    last_name = input('Ingrese su apellido: ')
    number = input('Ingrese su número de cuenta: ')
    balance = int(input('Ingrese su balance: '))

    cliente = Cliente(name, last_name, number, balance)
    return cliente


def inicio():
    cliente = instanciarCliente()
    opcion = 0
    while opcion != 4:
        while opcion < 4:
            print('1. Datos de la cuenta')
            print('2. Realizar un depósito')
            print('3. Realizar un retiro')
            print('4. Salir\n')
            opcion = int(input('Ingrese la opción deseada: '))
            if opcion > 4 or opcion < 0:
                print('No se ingreso una opción válida')
            if opcion == 1:
                print(cliente)
            elif opcion == 2:
                cliente.depositar()
            elif opcion == 3:
                print(f'Usted cuenta con {cliente.balance}')
                cliente.retirar()
            elif opcion == 4:
                print('Gracias por usar este servicio')


# MAIN

inicio()




