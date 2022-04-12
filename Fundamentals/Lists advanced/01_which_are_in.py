# searched_strings = input().split(", ")
# words = input().split(", ")
#
# substrings = []
#
# for string in searched_strings:
#     for word in words:
#         if string in word:
#             substrings.append(string)
#             break
#
# print(substrings)

searched_strings = input().split(", ")
sentence = input()

substrings = [el for el in searched_strings if el in sentence]
print(substrings)