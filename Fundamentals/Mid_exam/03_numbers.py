numbers = [int(el) for el in input(). split()]

average_value = sum(numbers) / len(numbers)
top_numbers = sorted([num for num in numbers if num > average_value], reverse=True)
if not top_numbers:
    print("No")
if len(top_numbers) > 5:
    print(*top_numbers[:5])
else:
    print(*top_numbers)

# n = int(input())
# previous_list = []
# for line in range(n):
#     current_list = []
#     for index in range(len(previous_list) + 1):
#         if index == 0:
#             current_list.append(1)
#         elif index == len(previous_list):
#             current_list.append(previous_list[-1])
#         else:
#             current_list.append(previous_list[index] + previous_list[index-1])
#     print(*current_list)
#     previous_list = current_list
#
