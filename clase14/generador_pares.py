def generador_pares():
    numero = 2
    while True:
        yield numero
        numero += 2


# Uso con un bucle for poniendo el límite desde fuera. Limite 10.
limite = 10
for par in generador_pares():
    if par > limite:
        break
    print(par)


class IteradorPares:

    def __init__(self, limite):
        self.limite = limite
        self.numero_actual = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.numero_actual > self.limite:
            raise StopIteration     # Detiene la iteración cuando se supera el límite

        resultado = self.numero_actual
        self.numero_actual += 2
        return resultado


# Uso con un bucle for
for par in IteradorPares(limite=17):
    print(par)
