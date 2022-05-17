text = list(input())

reverse_word = ""

for char in range(len(text)):
    reverse_word += text.pop()

print(reverse_word)
