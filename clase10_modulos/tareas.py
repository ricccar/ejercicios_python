# Lógica de creación de tareas
# Las tareas nunca deben de ser mayores de 20 caracteres

tareas = ["Tarea Test"]

def crea_tarea(tarea):
    tareas.append(tarea)
    print(f"Se ha creado la tarea: {tarea}")


def eliminar_tarea(indice):
    tarea_eliminada = tareas.pop(indice)
    print(f"Se ha eliminado la tarea: {tarea_eliminada}")


def mostrar_tarea(tarea):
    print(f"Tareas: {tareas}")
