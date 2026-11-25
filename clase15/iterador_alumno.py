class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas


alumno1 = Alumno("Ana", [8.5, 9.0, 7.2, 10])


iterador_notas = iter(alumno1.notas)

print(next(iterador_notas))
print(next(iterador_notas))
print(next(iterador_notas))
print(next(iterador_notas))
