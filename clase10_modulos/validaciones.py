# Validaciones de las tareas

# Validación 20 caracteres (o menos)

def valida_veinte(tarea: str) -> bool:
    if len(tarea)>20:
        return False
    else:
        return True