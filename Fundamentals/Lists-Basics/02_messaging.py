# numbers = input().split()
# text = list(input())
# message = ""
# sum_digits = 0
# for num in numbers:
#     list_numbers = list(num)
#     temp_list = []
#     sum_digits = 0
#     for index in range(len(list_numbers)):
#         temp_list.append(int(list_numbers[index]))
#         sum_digits = sum(temp_list)
#         if sum_digits > len(text):
#             sum_digits = sum_digits - len(text)
#     message += text[sum_digits]
#     text.pop(sum_digits)
#
# print(message)

numbers = input().split()
text = list(input())
message = ""
character_index = 0
for num in numbers:
    list_numbers = list(num)
    nums_as_int = [int(str) for str in list_numbers]
    character_index = sum(nums_as_int)
    if character_index > len(text) - 1:
        character_index = character_index - len(text)
    message += text[character_index]
    text.pop(character_index)
print(message)
