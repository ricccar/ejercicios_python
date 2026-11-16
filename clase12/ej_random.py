import random

# Dados

d6 = random.randint(1, 6)
print(d6)


dias_semana = "LMXJVSD"
dia_aleatorio = random.choice(dias_semana)
print(dia_aleatorio)

numeros_ordenados = list(range(10))
random.shuffle(numeros_ordenados)
print(numeros_ordenados)
