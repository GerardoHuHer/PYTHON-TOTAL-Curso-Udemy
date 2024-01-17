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

        deposito1 = int(input('Ingrese la cantidad de dinero que desea depositar: '))
        if deposito1 < 0:
            print('No puede depositar cantidades negativas')
        else:
            self.balance += deposito1
            return self.balance

    def retirar(self):
        retiro1 = int(input('Ingrese la cantidad de dinero que desea retirar: '))
        if (retiro1 > self.balance) or (retiro1 < 0):
            print('No puede realizar el retiro porque no tiene tal cantidad de dinero')
        else:
            print(f'Ha retirado ${retiro1}, su saldo actual es de {self.balance - retiro1}')
            self.balance = self.balance - retiro1
            return self.balance


# FUNCIONES


def instanciar_cliente():
    name = input('Ingrese su nombre: ')
    last_name = input('Ingrese su apellido: ')
    number = input('Ingrese su número de cuenta: ')
    balance = int(input('Ingrese su balance: '))

    cliente = Cliente(name, last_name, number, balance)
    return cliente


def switch(opc, cliente):
    opcion = {
        1: datos,
        2: deposito,
        3: retiro,
        4: salida
    }
    return opcion.get(opc, "No se ingresó una opción válida")(cliente)


def datos(cliente):
    print(cliente)


def deposito(cliente):
    cliente.depositar()


def retiro(cliente):
    print(f"Usted cuenta con {cliente.balance}")
    cliente.retirar()


def salida():
    print("Gracias por usar este servicio")


def inicio():
    cliente = instanciar_cliente()
    opcion = 0
    while opcion != 4:
        while opcion < 4:
            print('1. Datos de la cuenta')
            print('2. Realizar un depósito')
            print('3. Realizar un retiro')
            print('4. Salir\n')
            opcion = int(input('Ingrese la opción deseada: '))
            switch(opcion, cliente)

# MAIN

inicio()




