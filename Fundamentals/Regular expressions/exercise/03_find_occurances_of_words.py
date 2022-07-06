# import re
#
# text = input()
# searched_word = input()
# pattern = fr"\b{searched_word}\b"
#
# matches = re.findall(pattern, text, re.IGNORECASE)
# print(len(matches))

import re

text = input()
numbers = re.findall(r'\d+', text)
new_text = ""

for num in numbers:
    position = text.find(num)
    new_text += text[:position].upper() * int(num)
    text = text.replace(text[:position + len(num)], "")

unique = "".join(set(new_text))

print(f"Unique symbols used: {len(unique)}")
print(new_text)