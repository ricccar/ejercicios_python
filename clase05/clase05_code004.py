def square_sum(numbers):
    result = 0
    for n in numbers:
        result += n**2
    return result


print(square_sum([1, 2, 3, 5]))
