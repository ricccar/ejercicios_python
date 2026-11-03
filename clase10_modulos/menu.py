# Representación por pantalla

opciones = {
    1: "Crear tarea",
    2: "Ver tarea",
    3: "Eliminar tarea",
    4: "Salir"
}

def ver_menu():
    menu = "\nAPP PARA HACER TAREAS\n\n"
    for clave, valor in opciones.items():
        menu += f">\t{clave} - {valor}\n"
    print(menu)

