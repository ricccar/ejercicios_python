# Aquí crearemos las funciones que usaremos en la calculadora

def sumar (n1: float, n2: float) -> float:
    return n1 + n2

def restar (n1: float, n2: float) -> float:
    return n1 - n2

def multiplicar (n1: float, n2: float) -> float:
    return n1 * n2

def dividir (n1: float, n2: float) -> float:
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("No se puede dividir entre 0!")

def elevar (n1: float, n2: float) -> float:
    return n1 ** n2

def raiz (n1: float, n2: float) -> float:
    return n1 ** (1/n2)

print(raiz(27,3))
