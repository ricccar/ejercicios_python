"""Ejercicio (veamos como vamos con el temario):
 
Vamos a hacer el sistema de una sala de seguridad o cámara acorazada.
 
Tenemos que hacer un sistema de pasos independientes en los que se tienen que cumplir los siguientes:
 
Se tiene que presentar una tarjeta valida
Se tiene que introducir un PIN correctamente (para abrir la cámara o sala)
Se tiene que presentar una huella dactilar correcta
Los tres pasos anteriores deben realizarse en ese orden, y se deben de especificar por print, por separado
Si se produce un fallo, todo se reinicia y se debe empezar desde cero
Si se producen tres fallos consecutivos, el sistema se bloquea para siempre
 
puntos extra:
 
que el sistema sea facil de cambiar o mejorar, de forma que se puedan eliminar, añadir, modificar etc... pasos sin que ello
suponga rehacer el codigo
"""


# Crear métodos para verificar

tarjetas_validas = {
    "001": "ABCDEFG",
    "002": "BCFGHIZ",
    "003": "JCFGHIZ"
}
pins_validos = {
    "001": "1234",
    "002": "2233",
    "003": "2143"
}
huellas_validas = {
    "001": "AgdhashAghsghg",
    "002": "sgfsagfssgGAGG",
    "003": "akjsfidfdkmmks"
}


def paso_tarjeta(diccionario_tarjetas):
    print("\n--- PASO 1: Identificación con Tarjeta ---")
    tarjeta = input("Introduzca su tarjeta: ").strip()
    if tarjeta in diccionario_tarjetas.values():
        print("[OK] Tarjeta aceptada.")
        return True
    print("ERROR Tarjeta no válida.")
    return False


def paso_pin(diccionario_pins):
    print("\n--- PASO 2: Código de Seguridad ---")
    pin = input("Introduzca su PIN: ").strip()
    if pin in diccionario_pins.values():
        print("[OK] PIN correcto.")
        return True
    print("[ERROR] PIN incorrecto.")
    return False


def paso_huella(diccionario_huellas):
    print("\n--- PASO 3: Escáner Huellas ---")
    huella = input("Coloque su dedo en el lector (escriba 'código'): ").strip()
    if huella in diccionario_huellas.values():
        print("[OK] Huella dactilar verificada.")
        return True
    print("[ERROR] Huella no reconocida.")
    return False


pasos_seguridad = [
    (paso_tarjeta, tarjetas_validas),
    (paso_pin, pins_validos),
    (paso_huella, huellas_validas)
]


def ejecutar_sistema_seguridad():
    cuenta_fallos = 0
    maximo_intentos = 3

    print("=== SISTEMA DE SEGURIDAD ACTIVADO ===")

    while True:
        if cuenta_fallos >= maximo_intentos:
            print("\nEl sistema se ha bloqueado")
            break
        else:
            error_en_paso = False

        for paso_funcion, diccionario in pasos_seguridad:
            exito = paso_funcion(diccionario)

            if not exito:
                cuenta_fallos += 1
                print(
                    f"\nReiniciando sistema... (Fallos consecutivos: {cuenta_fallos}/{maximo_intentos})")
                error_en_paso = True
                break

        if not error_en_paso:
            print("\nAutorizado a la cámara acorazada.")
            break


ejecutar_sistema_seguridad()
