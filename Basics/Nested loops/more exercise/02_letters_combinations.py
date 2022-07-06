first_letter = input()
second_letter = input()
skip_letter = input()
counter = 0
start = ord(first_letter)
stop = ord(second_letter) + 1
skip = ord(skip_letter)
combinations = ""
for letter1 in range(start, stop):
    for letter2 in range(start, stop):
        for letter3 in range(start, stop):
            if letter3 != skip and letter2 != skip and letter1 != skip:
                counter += 1
                combinations +=f"{chr(letter1)}{chr(letter2)}{chr(letter3)} "
combinations += str(counter)
print(combinations)