def smallest_of_three(num1, num2, num3):
    smallest_number = min(num1, num2, num3)
    return smallest_number


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(smallest_of_three(number_1, number_2, number_3))