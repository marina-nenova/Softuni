# text = input()
# new_text = ""
# last_letter = ""
# for current_letter in text:
#     if current_letter != last_letter:
#         new_text += current_letter
#         last_letter = current_letter
#
# print(new_text)


text = input()
result = ""

while text != "":
    result += text[0]
    text = text.lstrip(text[0])

print(result)