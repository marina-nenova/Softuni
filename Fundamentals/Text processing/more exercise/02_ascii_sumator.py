first_char_code = ord(input())
second_char_code = ord(input())
text = input()
sum_chars = 0

for char in text:
    if first_char_code < ord(char) < second_char_code:
        sum_chars += ord(char)

print(sum_chars)