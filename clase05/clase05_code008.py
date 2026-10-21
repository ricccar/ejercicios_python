def first_dup(s):
    for index, l in enumerate(s.lower()):
        if l in s[index + 1:]:
            return l


print(first_dup("Grandielocu"))
print(first_dup("localocaloca"))
print(first_dup("Babiera"))
