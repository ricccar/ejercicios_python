class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas


class IteradorNotas:
    def __init__(self, alumno):
        self.notas = alumno.notas
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.notas):
            nota_actual = self.notas[self.indice]
            self.indice += 1
            return nota_actual
        else:
            raise StopIteration


# Uso
alumno = Alumno("Ricardo", [7.5, 9.2, 8.0])
mi_iterador = IteradorNotas(alumno)

print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
