# Creando la clase trabajador que hereda de persona.
class Persona:
    
     def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

     def andar(self):
        print(f"{self.nombre} está andando.")

class Trabajador(Persona):
     def percibir_salario(self, cantidad):
         print(f"{self.nombre} ha percibido {cantidad}€")

ric = Trabajador("Ricardo", 50)
ric.percibir_salario(1440)
