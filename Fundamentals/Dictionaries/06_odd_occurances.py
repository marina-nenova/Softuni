words = [word.lower() for word in input().split()]

dict_of_words = {}

for word in words:
    if word not in dict_of_words:
        dict_of_words[word] = 0
    dict_of_words[word] += 1

odd_occurrences = [key for key, value in dict_of_words.items() if value % 2 != 0]
print(*odd_occurrences)