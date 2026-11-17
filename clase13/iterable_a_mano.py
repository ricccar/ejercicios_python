# Iterable hecho a mano
from typing import Iterator

class Frase:
    def __init__(self, texto: str):
        self.frase = texto
        self.palabras = texto.split()   #Esto divide la frase en lista de palabras que le pasaremos al 

    def __iter__(self) -> Iterator:
        return IteradorFrases(self.palabras)    # Permite crear un iterador desde el iterable

# Iterador hecho a mano
class IteradorFrases:
    def __init__(self, palabras: list[str]):
        self.palabras = palabras    # Las palabras que tenemos en la lista de palabras
        self.indice = 0             # Índice para la iteración

    def __next__(self):
        try:
            palabra = self.palabras[self.indice]    # Vamos iterando palabra por palabra
        except IndexError:  # Si hemos recorrido el iterable entero, lanzamos excepción de StopIteration
            raise StopIteration()
        self.indice += 1    # Subimos uno el índice para que podamos iterar
        return palabra.upper()  # Para demostrar el iterable lo devolvemos en mayúsculas

    def __iter__(self) -> Iterator:     # no es necesario, pero permite cumplir con el ABC de los iteradores
        return self

# Lo probamos
frase = Frase("esto es una frase en mayúsculas!")   # Definimos la frase a iterar
iterador_frase = iter(frase)    # Creamos el iterador
try:
    print(next(iterador_frase))
    print(next(iterador_frase))
    print(next(iterador_frase))
    print(next(iterador_frase))
    print(next(iterador_frase))
    print(next(iterador_frase))
    print(next(iterador_frase))
    print(next(iterador_frase))
except StopIteration:
    print("Se ha parado la iteración (raise StopIteration)\n")

# Probamos la iteraciónb en un context manager
fr = Frase("mira como itero esta frase")
for palabra in fr:
    print(palabra)