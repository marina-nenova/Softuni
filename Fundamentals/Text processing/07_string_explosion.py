text = input()
new_text = ""
strength = 0

for index in range(len(text)):
    if text[index] != ">" and strength > 0:
        strength -= 1
    elif text[index] == ">":
        strength += int(text[index + 1])
        new_text += text[index]
    else:
        new_text += text[index]

print(new_text)
