# Lógica de creación de tareas
# Las tareas nunca deben de ser mayores de 20 caracteres
from validaciones import valida_veinte

tareas = []

def crea_tarea(tarea):
    if valida_veinte(tarea):
        tareas.append(tarea)
        print(f"Se ha creado la tarea: {tarea}")


def eliminar_tarea(indice):
    tarea_eliminada = tareas.pop(indice-1)
    print(f"Se ha eliminado la tarea: {tarea_eliminada}")


def mostrar_tarea():
    print(f"Tareas: {tareas}")
