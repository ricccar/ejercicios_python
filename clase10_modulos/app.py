# Escribimos el código

import menu
import tareas

while True:
    menu.ver_menu()
    opcion_elegida = int(input("Elige una opción: "))
    if opcion_elegida in menu.opciones:
        print(f"Has seleccionado: {menu.opciones[opcion_elegida]}")
        if opcion_elegida == 1:
            tarea_a_crear = input(f"Introduce la tarea que quieres crear: \n")
            tareas.crea_tarea(tarea_a_crear)
        elif opcion_elegida == 2:
            tareas.mostrar_tarea()
        elif opcion_elegida == 3:
            tarea_a_eliminar = int (input (f"Introduce el indice de la tarea que quieres eliminar: \n"))
            tareas.eliminar_tarea(tarea_a_eliminar) 
        else:
            break
        print("-"*30)