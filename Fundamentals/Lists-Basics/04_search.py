n = int(input())
searched_word = input()
all_texts = []
sorted_texts = []

for _ in range(n):
    text = input()
    all_texts.append(text)
    if searched_word in text:
        sorted_texts.append(text)
print(all_texts)
print(sorted_texts)