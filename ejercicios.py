"""# Repaso
nombre = "Ricardo"
print(nombre)
print(type(nombre))


# Tupla
variable = (1, 2, 3, 4)
print(variable)
print(type(variable))


# Lista
variable = [1, 2, 3, 4]
print(variable)
print(type(variable))


# Diccionario
variable = {
    "clave": "valor"
}

print(type(variable))
print(variable["clave"])


# Crear sistema de usuarios concontraseñas y emails.
usuarios = [
    ("Lola", "abc234", "lola@test.com"),
    ("Miguel", "abc234!", "miguel@test.com"),
    ("Juan", "micontrasena", "juan@test.com"),
    ("Marta", "abc1245", "marta@test.com")
]


# Lógica de programación
mi_usuario = input("Indica tu usuario: ")
mi_contraseña = input("Indica tu contraseña: ")
usuario_encontrado = False

for usuario in usuarios:
    if mi_usuario == usuario[0]:
        usuario_encontrado = True
        if mi_contraseña == usuario[1]:
            print("Usuario y contraseña correctos.")
        else:
            print("La contraseña no es correcta.")
if not usuario_encontrado:
    print("El usuario no fue encontrado")
"""

"""
# Crear sistema de usuarios concontraseñas y emails.
usuarios = {
    1: {"nombre": "Lola", "contraseña": "abc234", "email": "lola@test.com"},
    2: {"nombre": "Miguel", "contraseña": "abc234!", "email": "miguel@test.com"},
    3: {"nombre": "Juan", "contraseña": "micontrasena", "email": "juan@test.com"},
    4: {"nombre": "Luisa", "contraseña": "micontra", "email": None},
    5: {"nombre": "Marta", "contraseña": "abc1245", "email": "marta@test.com"}
}


# Lógica de programación
mi_usuario = input("Indica tu usuario: ")
mi_contraseña = input("Indica tu contraseña: ")
usuario_encontrado = False

for usuario in usuarios.values():
    if mi_usuario.lower() == usuario["nombre"].lower():
        usuario_encontrado = True
        if mi_contraseña == usuario["contraseña"]:
            print("Usuario y contraseña correctos.")
        else:
            print("La contraseña no es correcta.")
        if not usuario["email"]:
            nuevo_email = input("Tu usuario no tiene email, crea uno: \n")
            if nuevo_email.count("@") == 1:
                usuario["email"] = nuevo_email
            else:
                print("Ese email no fue válido.")
if not usuario_encontrado:
    print("El usuario no fue encontrado")
"""

# Vamos a hacer un menú

menu = """
#### Bienvenido al código de Tajamar! ####

1. Leer datos
2. Nueva entrada
3. Actualizar entrada
4. Salir

"""
print(menu)
comportamiento = {
    1: "leer datos",
    2: "crear entrada",
    3: "actualizar una entrada",
    4: "salir"
}

eleccion = None
while not eleccion:
    eleccion_usuario = int(input("¿Qué opción tomas?\n"))
    if eleccion_usuario in comportamiento:
        eleccion = eleccion_usuario
        break
    else:
        print("La elección no es válida!\n")

print(f"Has elegido la opcion{eleccion} ---> {comportamiento[eleccion]}")
