# Ejercicio
# Crear una función en la que me den una lista, la lista tendrá números y strings
# me tiene que devolver una tupla con todos los strings juntos en un único string, y por otra parte, los números sumados
# ejemplo:
# mi_funcion([1, 2, "a", "b", 3, "c"])
# debería de darme
# ("abc", 6)

lista = [1, 2, "a", 3, "b", "V", 5, 159, "sevilla"]
lista2 = [122, 22, "ahora", "forma", 31,
          "bar", "Valencia", 52, 1590, "sevilla"]


def separa_string_suma_numeros(l):
    cadena = ""
    suma = 0
    for elemento in l:
        if type(elemento) == str:
            cadena += elemento
        else:
            suma += elemento
    tupla = (cadena, suma)
    return tupla


print(separa_string_suma_numeros(lista))
print(separa_string_suma_numeros(lista2))
