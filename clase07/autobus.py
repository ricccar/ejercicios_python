class Autobus:
    def __init__(self, matricula, asientos_maximos):
        self.matricula = matricula
        self.asientos_maximos = asientos_maximos
        self.pasajeros_actuales = 0
        self.esta_arrancado = False  # El autobús empieza parado
 
    def arrancar(self):
        if self.esta_arrancado:
            print(f"El autobús {self.matricula} ya está arrancado.")
        else:
            self.esta_arrancado = True
            print(f"El autobús {self.matricula} ha arrancado.")
 
    def parar(self):
        if not self.esta_arrancado:
            print(f"El autobús {self.matricula} ya está parado.")
        else:
            self.esta_arrancado = False
            print(f"El autobús {self.matricula} se paró.")
 
    def subir_pasajeros(self, cantidad):
        asientos_libres = self.asientos_maximos - self.pasajeros_actuales
 
        if cantidad <= asientos_libres:
            self.pasajeros_actuales += cantidad
            print(
                f"Subieron {cantidad} pasajeros. Pasajeros actuales: {self.pasajeros_actuales} de {self.asientos_maximos} asientos máximos")
        else:
            print(f"No pueden subir {cantidad} pasajeros. No caben.")
 
    def bajar_pasajeros(self, cantidad):
        if cantidad <= self.pasajeros_actuales:
            self.pasajeros_actuales -= cantidad
            print(
                f"Bajaron {cantidad} pasajeros. Pasajeros actuales: {self.pasajeros_actuales} de{self.asientos_maximos} sientos máximos")
        else:
            print(
                f"No pueden bajar {cantidad} pasajeros. Solo hay {self.pasajeros_actuales} a bordo.")
 
 
bus_01 = Autobus("1234-AB", 40)
bus_01.arrancar()
bus_01.arrancar()
bus_01.subir_pasajeros(35)
bus_01.subir_pasajeros(10)
 
 
bus_02 = Autobus("5678-GD", 50)
bus_02.subir_pasajeros(20)
bus_02.bajar_pasajeros(5)
bus_02.bajar_pasajeros(30)
 
 
bus_03 = Autobus("9012-HZ", 25)
bus_03.parar()
bus_03.arrancar()
bus_03.parar()