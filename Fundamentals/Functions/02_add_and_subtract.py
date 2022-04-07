def sum_numbers(num1, num2):
    return num1 + num2


def subtract(sum_ints, num3):
    return sum_ints - num3


def add_and_subtract(num1, num2, num3):
    return subtract(sum_numbers(num1, num2), num3)


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_subtract(number_1, number_2, number_3))
