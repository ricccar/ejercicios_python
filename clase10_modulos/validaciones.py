# Validaciones de las tareas

# Validación 20 caracteres (o menos)

def valida_veinte(tarea: str) -> bool:
    if len(tarea)>20:
        print("La tarea es demasiado larga!")
        return False
    else:
        return True