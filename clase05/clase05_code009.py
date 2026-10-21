def array_diff(a, b):
    res = []
    for j in a:
        if j not in b:
            res.append(j)
    return res


print(array_diff([1, 2, 2], [2]))
print(array_diff([1, 2, 4, 6, 6, 8, 9], [2, 6, 9]))
print(array_diff([10, 21, 22, 45], [2, 45, 20]))
