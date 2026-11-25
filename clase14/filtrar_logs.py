from pathlib import Path

def filtrar_logs(archivo, error):
    with Path(archivo).open("r") as fichero:
        for linea in fichero:
            if error.upper() in linea.upper():
                yield linea.strip()



opciones = {
    1: "ERROR",
    2: "DEBUG",
    3: "WARNING",
    4: "Salir"
}

def ver_menu():
    menu = "\nAPP PARA FILTRAR LOGS\n\n"
    for clave, valor in opciones.items():
        menu += f">\t{clave} - {valor}\n"
    print(menu)
    opcion_elegida = int(input("Elige una opción: "))

ver_menu()