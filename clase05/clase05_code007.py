def create_phone_number(n):
    numeros = ""
    for numero in n:
        numeros += str(numero)
    parte_1 = numeros[:3]
    parte_2 = numeros[3:6]
    parte_3 = numeros[6:]
    return f"({parte_1}) {parte_2}-{parte_3}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 2, 1, 3, 5, 0, 3, 7, 0, 9]))
