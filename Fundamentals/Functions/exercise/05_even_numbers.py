def check_even(number):
    if number % 2 == 0:
        return True

    return False


numbers = [int(el) for el in input().split()]

even_numbers_iterator = filter(check_even, numbers)
even_numbers = list(even_numbers_iterator)

print(even_numbers)


# numbers = [int(el) for el in input(). split()]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)
