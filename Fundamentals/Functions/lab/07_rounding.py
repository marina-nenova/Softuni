# def round_numbers(numbers_list):
#     rounded_list = []
#     for number in numbers_list:
#         rounded_list.append(round(number))
#     return rounded_list
#
#
# numbers = [float(num) for num in input().split()]
#
# print(round_numbers(numbers))


numbers = [float(num) for num in input().split()]
rounded_numbers = [round(num) for num in numbers]
print(rounded_numbers)