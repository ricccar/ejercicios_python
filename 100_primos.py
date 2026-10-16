def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


primos = [1]
num = 2
while len(primos) < 100:
    if es_primo(num):
        primos.append(num)
    num += 1

print("Los 100 primeros números primos son: " + str(primos))
