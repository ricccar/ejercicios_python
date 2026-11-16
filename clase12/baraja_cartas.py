# Crear baraja de cartas y barajarla

import random

palos = ("Oros", "Copas", "Espadas", "Bastos")
valores = ("As", "2", "3", "4", "5", "6", "7", "Sota", "Caballo", "Rey")


class Carta:
    def __init__(self, valor: str, palo: str):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"


class Baraja:
    def __init__(self):     # Perfecto
        self.cartas = [Carta(valor, palo)
                       for palo in palos for valor in valores]

    def barajar(self):
        random.shuffle(self.cartas)
        print("Se ha barajado la baraja")

    def mostrar(self):
        for carta in self.cartas:
            print(carta)


baraja = Baraja()
baraja.mostrar()
baraja.barajar()
baraja.mostrar()
