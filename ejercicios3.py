"""Ejercicio
 
Crear una función en la que me den una lista, la lista tendrá números y strings
 
me tiene que devolver una tupla con todos los strings juntos en un único string, y por otra parte, los números sumados
 
ejemplo:
 
mi_funcion([1, 2, "a", "b", 3, "c"])
 
debería de darme
 
("abc", 6)"""

"""
Ejercicio

Crear una funcion formatear_nombre a la que le demos por posición el nombre, el apellido,
y el apellido 2 de alguien, y que tenga dos args extra como clave valor, uno que sea upper 
(por defecto False) que ponga todo en mayúscula, y otro que sea añadir, y que añada un texto
al final en una línea nueva (con "\n")

una vez hecho esto, quiero que lo hagamos con empaquetamiento, ya que habrá nombres con solo un apellido,
o nombres con 2 nombres (y por tanto con 4 strings), es decir, habrá que usar empaquetamiento por posicion

    
"""


def formatear_nombre(*nombre_apellido1_apellido2, upper=False, añadir=None):
    nombre_completo = " ".join(str(p) for p in nombre_apellido1_apellido2)

    if upper:
        nombre_completo = nombre_completo.upper()

    if añadir is not None:
        nombre_completo += "\n" + str(añadir)

    return nombre_completo


# Pruebas
print(formatear_nombre("Luis", "López", "Fuentes"))
print(formatear_nombre("Luis", "López", "Fuentes", upper=True))
print(formatear_nombre("Luis", "Alberto", "López", "Fuentes", añadir="Saludos"))
print(formatear_nombre("Luis", añadir="Saludos"))
