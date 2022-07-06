def factorials_finder(number):
    factorial = 1
    for num in range(2, number + 1):
        factorial *= num
    return factorial


number_1 = int(input())
number_2 = int(input())

number_1_factorial = factorials_finder(number_1)
number_2_factorial = factorials_finder(number_2)

division = number_1_factorial / number_2_factorial
print(f"{division:.2f}")
