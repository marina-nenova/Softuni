import re

text = input()
pattern = r"\+359([-\s])2(\1)\d{3}(\1)\d{4}($|(?=[,\s]))"
valid_numbers = re.finditer(pattern, text)

for num in valid_numbers:
    print(num.group())

for num in valid_numbers:
    print(num.group())


# valid_numbers = [num.group() for num in valid_numbers]
# print(*valid_numbers, sep=", ")
