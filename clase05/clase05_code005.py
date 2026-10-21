def sum_two_smallest_numbers(numbers):
    minimo = min(numbers)
    numbers.remove(minimo)
    return (minimo+min(numbers))


print(sum_two_smallest_numbers([2, 5, 6, 9, 34]))
print(sum_two_smallest_numbers([223, 533, 611, 911, 34]))
print(sum_two_smallest_numbers([12, 15, 26, 19, 0]))
