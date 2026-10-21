"""Ejercicio
 
Crear una funcion formatear_nombre a la que le demos por posición el nombre, el apellido, y el apellido 2 de alguien, y que tenga dos args extra como clave valor, uno que sea upper (por defecto False) que ponga todo en mayúscula, y otro que sea añadir, y que añada un texto al final en una línea nueva (con "\n")
 
una vez hecho esto, quiero que lo hagamos con empaquetamiento, ya que habrá nombres con solo un apellido, o nombres con 2 nombres (y por tanto con 4 strings), es decir, habrá que usar empaquetamiento por posicion
 
"""


def formatear_nombre(*nombre_apellidos, upper=False, anadir=""):
    formateando = " ".join(nombre_apellidos) + "\n" + anadir
    if upper:
        return formateando.upper()
    else:
        return formateando


print(formatear_nombre("Ricardo", "Lamelas",
      "Labrada", upper=False, anadir="Regards"))
print(formatear_nombre("Ricardo", "Lamelas",
      "Labrada", upper=True, anadir="Regards"))
print(formatear_nombre("Ricardo", "Lamelas", "Labrada"))
print(formatear_nombre("Ricardo", "Lamelas", upper=True, anadir="Regards"))
print(formatear_nombre("Ricardo", anadir="Saludos"))
