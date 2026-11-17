class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas


def obtener_notas(alumno):
    for nota in alumno.notas:
        yield nota


alumno1 = Alumno("Carlos", [6.0, 7.5, 8.0])
mi_iterador = obtener_notas(alumno1)

print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
