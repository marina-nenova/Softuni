# numbers = input()
# numbers_list = numbers.split(" ")
# opposite_list = []
# for element in numbers_list:
#     if int(element) < 0:
#         opposite_list.append(abs(int(element)))
#     elif int(element) > 0:
#         opposite_list.append(-abs(int(element)))
#     else:
#         opposite_list.append(int(element))
#
# print(opposite_list)

numbers = [int(num) for num in input().split()]

print([abs(num) if num < 0 else -abs(num) for num in numbers])