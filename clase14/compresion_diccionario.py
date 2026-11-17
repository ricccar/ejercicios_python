"""
Ejercicio
Crear una comprensión de lista que tome un diccionario con alumnos y una nota para cada uno de ellos, y me devuelva sus notas
convertidas en la siguiente regla de tres: las notas van de 1 a 20, y tenemos que dividir por 4 para que en la lista tenga las
notas de 1 a 5. Crear un generador que me vaya dando números desde el 0.0 a un numero limite, y que vaya dando en incrementos
de 0.1, es decir, 0.0, ,0.1, 0.2, 0.3, ... 
puntos extra si para el ejercicio de los alumnos y para el ejercicio del generador usamos numeros aleatorios para generar estas
notas de alumnos o este limite de generador!
"""

import random

# Lista de alumnos de ejemplo
alumnos = ["Ana", "Carlos", "Elena", "David", "Sofía"]

# Generamos el diccionario con notas aleatorias entre 1 y 20
notas_iniciales = {alumno: random.randint(1, 20) for alumno in alumnos}
print("Notas iniciales (1 a 20):", notas_iniciales)


# Comprensión de lista devolviendo el alumno y su nota convertida
notas_convertidas = [
    (alumno, round(nota / 4, 2))
    for alumno, nota in notas_iniciales.items()
]

print("\nNotas convertidas (1 a 5):")
for alumno, nota in notas_convertidas:
    print(f"- {alumno}: {nota}")


def generador_decimales(limite):
    actual = 0.0
    # Usamos <= para incluir el límite si coincide exactamente con un incremento
    while actual <= limite:
        yield round(actual, 1)
        actual += 0.1


# Generamos un límite aleatorio entre 0.0 y 5.0 (redondeado a 1 decimal)
limite_aleatorio = round(random.uniform(0.0, 5.0), 1)
print(f"\nLímite aleatorio generado: {limite_aleatorio}\n")

# Ejecutamos el generador
print("Secuencia generada:")
for numero in generador_decimales(limite_aleatorio):
    print(str(numero) + ",  ")

# Código de compañero
notas_dict = {
    "Jose": random.randint(1, 20),
    "Ana": random.randint(1, 20),
    "Luis": random.randint(1, 20),
    "Pedro": random.randint(1, 20),
    "Lucia": random.randint(1, 20),
    "Martin": random.randint(1, 20),
}

print(notas_dict)

notas = [nota / 4 for nota in notas_dict.values()]

print(notas)


def generar_numeros_escala(limite):
    numero = 0.0

    while numero < limite + 0.1:
        yield round(numero, 1)
        numero += 0.1


for numero in generar_numeros_escala(random.randint(1, 5)):
    print(numero)
