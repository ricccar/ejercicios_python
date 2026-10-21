def century(year):
    if year % 100 == 0:
        return (year/100)
    else:
        return ((year//100)+1)


print(century(1995))
print(century(1))
print(century(1695))
print(century(1001))
