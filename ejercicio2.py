# Encontrar el máximo de una lista de números

def maximo_de_lista(mi_lista):
    """
    Función que recibe una lista de números y haya su máximo

    Args:
        mi_lista (_type_): _description_
    """
    # Validación de parámetro que recibe
    if not isinstance(mi_lista, list):
        raise TypeError("El parámetro debe ser una lista.")

    maximo = 0
    for numero in mi_lista:
        if numero > maximo:
            maximo = numero

    return (maximo)


prueba = [1, 2, 3, 5, 7, 1521, 1, 7, 8, 90, 4, 56, 15, 125, 222]
print(maximo_de_lista(prueba))

"""
2-  Conseguir que dos variables que son listas se conviertan en una única
variable que sea un diccionario (la primera lista serán las claves y la segunda
serán los valores)
Ejemplo

lista_1 = [1,2,3]
lista_2 = ["a", "b", "c"]

el resultado debería ser

diccionario = {1: "a", 2: "b", 3: "c"}
"""


def unir_dos_listas_en_diccionario(lista_claves, lista_valores):
    """
    Función que recibe dos listas, una de claves y otra de valores y devuelve un diccionario fusionando las listas

    Args:
        lista_claves (_type_): _description_
        lista_valores (_type_): _description_
    """
# Validación: ambas listas deben tener la misma longitud
    if len(lista_claves) != len(lista_valores):
        raise ValueError(
            "Las listas deben tener la misma longitud para formar un diccionario.")

# Crear el diccionario usando zip
    return dict(zip(lista_claves, lista_valores))


lista_1 = [1, 2, 3, 4]
lista_2 = ["a", "b", "c", "d"]

diccionario = unir_dos_listas_en_diccionario(lista_1, lista_2)
print(diccionario)


"""
3- Conseguir que un diccionario se convierta en dos variables distintas, una lista de sus claves y una lista de sus valores
"""
diccionario = {
    1: {"nombre": "Ricardo", "apellidos": "Lamelas",
        "edad": 45, "teléfono": "666666666"},
    2: {"nombre": "Lucas", "apellidos": "López", "edad": 35, "teléfono": "697979797"},
    3: {"nombre": "María", "apellidos": "Pereira",
        "edad": 25, "teléfono": "645454545"}
}

claves = list(diccionario.keys())
valores = list(diccionario.values())
print(claves)
print(valores)


"""
4 - Hacer un sistema que valide DNIs

(tienen 8 numeros y un noveno carácter que es una letra mayuscula)
"""
