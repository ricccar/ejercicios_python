class Paciente:
    def __init__(self, nombre: str, enfermedad: str = None):
        self.nombre = nombre
        self.enfermedad = enfermedad


class Medico:
    def __init__(self, nombre: str, especialidad: str):
        self.nombre = nombre
        self.especialidad = especialidad

    def curar(self, paciente: Paciente):
        if paciente.enfermedad:
            print(
                f"El Dr. {self.nombre} está tratando a {paciente.nombre} por {paciente.enfermedad}")
            paciente.enfermedad = None
            print(f"¡{paciente.nombre} ha sido curado con éxito!")
        else:
            print(
                f"{paciente.nombre} ya se encuentra sano. ¡No necesita tratamiento!")


doctor = Medico("Ramón", "Med. General")


paciente1 = Paciente("Carlos", "Gripe")
paciente2 = Paciente("Sofía", "Fiebre alta")
paciente3 = Paciente("Mateo", "Gastritis")

sala_de_espera = [paciente1, paciente2, paciente3]

for p in sala_de_espera:
    print(f"Paciente: {p.nombre} Enfermedad: {p.enfermedad}")

for p in sala_de_espera:
    doctor.curar(p)


for p in sala_de_espera:
    print(f"Paciente: {p.nombre} Enfermedad: {p.enfermedad}")
