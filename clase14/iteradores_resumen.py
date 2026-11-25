
# Protocolo de iteración
# 1. Iterable (string, lista, diccionario)
# 2. Iterable ---> Iterador (iter())
# 3. Iteración del ieterador (con next())
# 4. Terminada, se tiene un error StopIteration que hace que pare

iterable = [1, 4, 5]

for elemento in iterable:   # Bucle for
    print(elemento)

iterador = iter(iterable)   # Bucle for
while True:
    try:
        elemento = next(iterador)
        print(elemento)
    except StopIteration:
        break


# Protocolo de Generador, el mismo for

def generador_print(iterable):
    iterador = iter(iterable)
    while True:
        try:
             yield next(iterador)
        except StopIteration:
            break

for numero in generador_print([1, 2, 3]):
    print(numero)

# Devolver números elevados al cuadrado

def generador_cuadrados(iterable):
    for elemento in iterable:
        yield elemento ** 2

for numero in generador_cuadrados([1, 2, 3]):
    print(numero)


# Sintaxis especial generadores ---> Comprensiones

var = (elemento for elemento in iterable if elemento > 0)    
print(var)                   # Generador
var = [elemento ** 2 for elemento in iterable if elemento > 0]                  # Lista
print(var)
var = {str(elemento): elemento for elemento in iterable if elemento > 0}        # Diccionario
print(var)


