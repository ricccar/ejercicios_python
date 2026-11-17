# bucle for no existe para python

for elemento in range(10):
    print(elemento)


# Protocolos con __iter___ y __next__

# Iterable: string, lista, tupla, diccionario, ... permite generar un iterador
iterable = "Cadena de caracteres"

# Iterador: elemento que puedo ietrar
iterador = iter(iterable)

print(iterador, type(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
#print(next(iterador))       # Error StopIteration, se finaliza el iterador

# Creamos un for manual con iterador
var = "Hola"        # Ejemplo String
var2 = [1,2,3,4,6,8,90]         # Ejemplo lista
it = iter(var2)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# En realidad iter y next son los métodos __iter__ y __next__ de un objeto 