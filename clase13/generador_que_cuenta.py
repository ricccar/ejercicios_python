# Generador que cuenta

def contador(limite = 1):
    cuenta = 0
    while cuenta < limite:
        cuenta += 1
        yield cuenta    # Return, como si fuuera el next

gen = contador(10)      # Como si fuera mi iter

for numero in gen:
    print(numero)


# No haría falta el gen y podría contener más de un yield
