class Ordenador:
    marca = "Lenovo"
    peso = 2.5
    sistema_operativo = "Windows 11"
    encendido = False

    def encender():
        """Método para encender el ordenador."""
        if not Ordenador.encendido:
            Ordenador.encendido = True
            print(
                f"El ordenador {Ordenador.marca} se ha encendido. Cargando {Ordenador.sistema_operativo}...")
        else:
            print(f"El ordenador {Ordenador.marca} ya está encendido.")


print(
    f"Este ordenador {Ordenador.marca} tiene {Ordenador.sistema_operativo} y pesa {Ordenador.peso}kg")

Ordenador.encender()
Ordenador.encender()
