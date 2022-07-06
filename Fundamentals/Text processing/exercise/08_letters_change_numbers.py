def convert_letter_to_num(letter):
    letter_position = 0
    if letter.islower():
        letter_position = ord(letter) - 96
    elif letter.isupper():
        letter_position = ord(letter) - 64
    return letter_position


sequence = [s.strip() for s in input().split()]
total_sum = 0

for string in sequence:
    string_sum = 0
    first_letter = string[0]
    last_letter = string[-1]
    string = string.lstrip(first_letter)
    string = string.rstrip(last_letter)
    number = int(string)

    first_num = convert_letter_to_num(first_letter)
    last_num = convert_letter_to_num(last_letter)

    if first_letter.isupper():
        string_sum += number / first_num
    elif first_letter.islower():
        string_sum += number * first_num
    if last_letter.isupper():
        string_sum -= last_num
    elif last_letter.islower():
        string_sum += last_num

    total_sum += string_sum

print(f"{total_sum:.2f}")
