def int_to_char(word):
    letters = list(word)
    num_as_str = []
    while letters[0].isdigit():
        num_as_str.append(letters[0])
        letters.pop(0)
    num = int("".join(num_as_str))
    letters.insert(0, chr(num))
    return "".join(letters)


def switch_letters(word):
    letters = list(word)
    letters[1], letters[-1] = letters[-1], letters[1]
    return "".join(letters)


message = input().split()
secret_message = [switch_letters(int_to_char(word)) for word in message]
print(" ". join(secret_message))

