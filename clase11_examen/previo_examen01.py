"""
Hacer un sistema de gestión de alumnos donde podamos crear, eliminar y 
modificar alumnos de un curso de Python
los alumnos tienen nombre, edad y una descripción
puntos extra: estos alumnos estudian Python, pero seria genial que el sistema nos permita 
crear alumnos especiales que estudien PHP, Javascript, Java, ...
"""


class Alumno:
    def __init__(self, _id: int, nombre: str, apellidos: str, edad: int, lenguaje: str = "Python"):
        self._id = _id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.lenguaje = lenguaje  # Permite Python, PHP, Java, etc.


class Gestion:
    def __init__(self):
        self.alumnos = {}
        self.contador_id = 1

    def crear_alumno(self):
        print("\n*** CREAR ALUMNO ***")
        nombre = input("Introduce su nombre: ")
        apellidos = input("Introduce sus apellidos: ")
        while True:
            try:
                edad = int(input("Edad: "))
                break
            except ValueError:
                print("Por favor, introduce un número válido para la edad.")

        lenguaje_opcion = input(
            "Lenguaje para su matrícula ('Python' si lo deja vacío): ").strip()
        if lenguaje_opcion:
            lenguaje = lenguaje_opcion
        else:
            lenguaje = "Python"

        nuevo_alumno = Alumno(self.contador_id, nombre,
                              apellidos, edad, lenguaje)
        self.alumnos[self.contador_id] = nuevo_alumno
        print(f"Alumno creado con éxito! ID: {self.contador_id}")
        self.contador_id += 1

    def mostrar_alumnos(self):
        print("\n*** LISTA DE ALUMNOS ***")
        if not self.alumnos:
            print("No hay alumnos registrados en el sistema.")
            return
        for alumno in self.alumnos.values():
            print(
                f"ID: {alumno._id} --> Nombre: {alumno.nombre} {alumno.apellidos} Lenguaje: {alumno.lenguaje}")
        print("-" * 40)

    def eliminar_alumno(self):
        print("\n*** ELIMINAR ALUMNO ***")
        try:
            id_alumno = int(input("Introduce el ID del alumno a eliminar: "))
            if id_alumno in self.alumnos:
                eliminado = self.alumnos.pop(id_alumno)
                print(f"¡Alumno {eliminado.nombre} eliminado correctamente!")
            else:
                print("Error: No se encontró ningún alumno con ese ID.")
        except ValueError:
            print("ID inválido.")

    def modificar_alumno(self):
        print("\n*** MODIFICAR ALUMNO ***")
        try:
            id_alumno = int(input("Introduce el ID del alumno a modificar: "))
            if id_alumno in self.alumnos:
                alumno = self.alumnos[id_alumno]
                print(f"\nModificando a: {alumno.nombre}")

                # Si se deja en blanco, conserva el valor actual
                nuevo_nombre = input(
                    f"Nuevo nombre [{alumno.nombre}]: ") or alumno.nombre
                nuevo_apellidos = input(
                    f"Nuevo/s apellido/s [{alumno.apellidos}]: ") or alumno.apellidos
                nueva_edad_input = input(f"Nueva edad [{alumno.edad}]: ")
                nueva_edad = int(
                    nueva_edad_input) if nueva_edad_input else alumno.edad
                nuevo_lenguaje = input(
                    f"Nuevo lenguaje [{alumno.lenguaje}]: ") or alumno.lenguaje

                # Actualizar datos
                alumno.nombre = nuevo_nombre
                alumno.apellidos = nuevo_apellidos
                alumno.edad = nueva_edad
                alumno.lenguaje = nuevo_lenguaje
                print("¡Datos modificados con éxito!")
            else:
                print("Error: No se encontró ningún alumno con ese ID.")
        except ValueError:
            print("Entrada inválida.")


def menu():
    sistema = Gestion()

    # Alumnos de prueba iniciales
    sistema.alumnos[1] = Alumno(1, "Ana", "Gómez", 23, "Python")
    sistema.alumnos[2] = Alumno(2, "Carlos",  "Pérez", 30, "PHP")
    sistema.contador_id = 3

    while True:
        print("\n=================================")
        print("  SISTEMA DE GESTIÓN DE ALUMNOS  ")
        print("=================================")
        print("1. Crear Alumno")
        print("2. Mostrar Alumnos")
        print("3. Modificar Alumno")
        print("4. Eliminar Alumno")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            sistema.crear_alumno()
        elif opcion == "2":
            sistema.mostrar_alumnos()
        elif opcion == "3":
            sistema.modificar_alumno()
        elif opcion == "4":
            sistema.eliminar_alumno()
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


menu()
