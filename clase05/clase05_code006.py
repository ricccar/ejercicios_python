def filter_list(l):
    lista_final = []
    for elemento in l:
        if type(elemento) == str:
            continue
        else:
            lista_final.append(elemento)
    return lista_final


print(filter_list(["a", 1, 2, "b"]))
print(filter_list([45, 123, "algo", "tú", 101, 2205, "banco", "gana"]))
print(filter_list([0, 1, 2, 4]))
print(filter_list(["0", "1", "2", "4"]))
