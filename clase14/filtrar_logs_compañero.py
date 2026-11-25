from pathlib import Path

def filtrar_logs(archivo, keyword):
    with Path(archivo).open("r") as fichero:
        for linea in fichero:
            if keyword.upper() in linea.upper():
                yield linea.strip()

menu = '''Introduce para filtrar los logs: 
           1- ERROR
           2- WARNING
           3 - INFO
           4 - Salir\n '''

while True:
    valor = int(input(menu))
    print(f"Valor recibido: {valor}, Tipo: {type(valor)}")
    match valor:
        case 1:
            keyword = "ERROR"
        case 2:
            keyword = "DEBUG"
        case 3:
            keyword = "WARNING"
        case 4: 
            break
        case _: 
            print("Valor no válido")
            continue

    for log in filtrar_logs("clase14\logs.txt", keyword):
        print(log)