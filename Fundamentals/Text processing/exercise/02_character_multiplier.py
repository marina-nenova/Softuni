strings = input().split()

shorter_word_length = min(len(strings[0]), len(strings[1]))
longer_word_length = max(len(strings[0]), len(strings[1]))
word_one = strings[0]
word_two = strings[1]

total_sum = 0
for index in range(shorter_word_length):
    total_sum += ord(word_one[index]) * ord(word_two[index])

for index in range(shorter_word_length, longer_word_length):
    if len(word_one) > len(word_two):
        total_sum += ord(word_one[index])
    else:
        total_sum += ord(word_two[index])

print(total_sum)
