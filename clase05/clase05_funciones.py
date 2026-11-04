# Función para invertir una lista:

def invertir(lista: list) -> list:
    return lista[::-1] if type (lista) == list else "Solo puedo invertir listas"

lista_prueba = [1, 2, 4, 6, 18, 23]
tupla_prueba = (1, 3, 6, 5, 8)
cadena = "Micadena"
print(invertir(lista_prueba))
print(invertir(tupla_prueba))
print(invertir(cadena))


# Función con parámetros pasados por clave valor.

def restar(n1, n2):
    return(n1-n2)

print(restar(n1=20, n2=5))      # 20-5
print(restar(n2=20, n1=5))      # 5-20


# Función con parámetro predefinido

def decir_hola(nombre = "no te conozco"):
    return f"Hola, {nombre}!"

print(decir_hola("Fernando"))   # Valor pasado como parámetro
print(decir_hola())             # Valor predefinido por no pasarle diucho parámetro


# Funciones con parámetros por orden / obliga a pasarlo antes por posición, * obliga a que después vayan por clave/valor

def titulo(texto, /, filigrana="~", *, ancho=50):
    print(f" {texto} ".center(ancho, filigrana))

titulo("El gran Lebowsky", "-", ancho=80)
titulo("Caminando entre lobos", "#")
titulo("American Beauty", filigrana="*")
titulo("Juarsic Park", filigrana="=", ancho=120)
titulo("La milla verde", ancho=20)


# Función variádica

def sumar(*numeros):        # Función variádica -----> convierte los parámetros en una tupla
    return sum(numeros)

print (sumar(23, 45, 23, 4, 3, 12))         # Por posición ------> 6 números
