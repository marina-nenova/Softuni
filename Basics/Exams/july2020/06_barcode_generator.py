# import math
#
# first_number = int(input())
# second_number = int(input())
#
# fourth_range_start = first_number % 10
# first_number = math.floor(first_number / 10)
# fourth_range_end = second_number % 10
# second_number = math.floor(second_number / 10)
#
# third_range_start = first_number % 10
# first_number = math.floor(first_number / 10)
# third_range_end = second_number % 10
# second_number = math.floor(second_number / 10)
#
# second_range_start = first_number % 10
# first_number = math.floor(first_number / 10)
# second_range_end = second_number % 10
# second_number = math.floor(second_number / 10)
#
# first_range_start = first_number
# first_range_end = second_number
#
# for num1 in range(first_range_start, first_range_end + 1):
#     for num2 in range(second_range_start, second_range_end + 1):
#         for num3 in range(third_range_start, third_range_end + 1):
#             for num4 in range(fourth_range_start, fourth_range_end + 1):
#                 if num1 % 2 == 1 and num2 % 2 ==1 and num3 % 2 == 1 and num4 % 2 == 1:
#                     print(f"{num1}{num2}{num3}{num4}", end = " ")

first_number = input()
second_number = input()

for num1 in range(int(first_number[0]), int(second_number[0])):
    for num2 in range(int(first_number[1]), int(second_number[1])):
        for num3 in range(int(first_number[2]), int(second_number[2])):
            for num4 in range(int(first_number[3]), int(second_number[3])):
                if num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 == 1 and num4 % 2 == 1:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")