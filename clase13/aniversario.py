"""
Ejercicio de fechas:
Crear una función que nos permita calcular cuantos días quedan hasta
nuestro aniversario (si no tenemos aniversario, hasta san valentin)
si quedan menos de 10 días, debería apurarnos a comprar un regalo y a preparar algo especial!
ademas, crear una segunda función que nos permita cambiar cuando es nuestro aniversario (o dia de san valentin)
truco: tendremos que usar correctamente el scope y tendremos que tener
un bucle para que el usuario vaya jugando con las fechas)
"""
from datetime import date

# Variables globales
# Por defecto, la fecha es Cumpleaños (7 de marzo)
mes_especial = 3
dia_especial = 7
nombre_evento = "Cumpleaños"


def calcular_dias_restantes():
    """Calcula los días que faltan para la fecha guardada y muestra alertas."""
    hoy = date.today()
    # Creamos la fecha del evento para este año
    fecha_evento = date(hoy.year, mes_especial, dia_especial)

    # Si la fecha ya pasó este año, calculamos para el año que viene
    if fecha_evento < hoy:
        fecha_evento = date(hoy.year + 1, mes_especial, dia_especial)

    dias_restantes = (fecha_evento - hoy).days

    print(
        f"\nHoy es {hoy.strftime('%d/%m/%Y')}. Tu próxima fecha ({nombre_evento}) es el {fecha_evento.strftime('%d/%m/%Y')}."
    )

    if dias_restantes == 0:
        print(f"¡HOY ES {nombre_evento.upper()}! ¡A celebrarlo!")
    elif dias_restantes < 10:
        print(f"¡Faltan solo {dias_restantes} días!")
        print(
            "Deberías ir a comprar un regalo y a preparar las velas."
        )
    else:
        print(
            f"Faltan {dias_restantes} días. Todavía tienes mucho tiempo."
        )


def cambiar_fecha():
    # Usamos 'global'
    global mes_especial, dia_especial, nombre_evento

    print("\n*** CONFIGURAR NUEVA FECHA ***")
    nuevo_nombre = input(
        "¿Qué celebramos? (Ej: Cumpleaños) : "
    )
    if nuevo_nombre.strip() != "":
        nombre_evento = nuevo_nombre
    else:
        nombre_evento = "Cumpleaños"

    try:
        nuevo_dia = int(input("Introduce el día (1-31): "))
        nuevo_mes = int(input("Introduce el mes (1-12): "))

        # Validamos que la fecha sea real.
        # Usamos un año bisiesto (2024) por si alguien cumple años el 29 de febrero
        date(2024, nuevo_mes, nuevo_dia)

        # Si no da error, actualizamos las variables globales
        dia_especial = nuevo_dia
        mes_especial = nuevo_mes
        print(
            f"¡Listo! Fecha actualizada al {dia_especial}/{mes_especial} ({nombre_evento})."
        )

    except ValueError:
        print(
            "Error: Has introducido una fecha inválida o texto en lugar de números. No se cambió el día."
        )


# --- BUCLE PRINCIPAL ---
def iniciar_programa():
    print("RECORDATORIO DIA ESPECIAL")

    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Ver cuántos días faltan")
        print("2. Cambiar la fecha de aniversario")
        print("3. Salir")

        opcion = input("Elige una opción (1,2,3): ")

        if opcion == "1":
            calcular_dias_restantes()
        elif opcion == "2":
            cambiar_fecha()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


iniciar_programa()
