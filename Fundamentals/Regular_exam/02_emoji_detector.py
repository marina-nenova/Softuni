# import re
#
# text = input()
# digits_pattern = r"\d"
# emoji_pattern = r"(::|\*\*)[A-Z][a-z]{2,}\1"
# cool_threshold = 1
#
# for num in re.findall(digits_pattern, text):
#     cool_threshold *= int(num)
#
# emojis = list(re.finditer(emoji_pattern, text))
#
# print(f"Cool threshold: {cool_threshold}")
# print(f"{len(emojis)} emojis found in the text. The cool ones are:")
#
# for emoji in emojis:
#     emoji_value = sum(ord(char) for char in emoji.group() if char.isalpha())
#     if emoji_value >= cool_threshold:
#         print(emoji.group())


import re
expression = r'(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})(\1)'
text = input()
cool_threshold = 1
emoji_counter = 0
list_cool = []
for ch in text:
    if ch.isdigit():
        cool_threshold *= int(ch)
print(f'Cool threshold: {cool_threshold}')
matches = re.findall(expression, text)
for match in matches:
    emoji_coolness = 0
    emoji = ''.join(match)
    emoji_counter += 1
    for n in emoji:
        if n not in ['*', ':']:
            emoji_coolness += ord(n)
    if emoji_coolness >= cool_threshold:
        list_cool.append(emoji)

print(f'{emoji_counter} emojis found in the text. The cool ones are:')
for e in list_cool:
    print(e)
