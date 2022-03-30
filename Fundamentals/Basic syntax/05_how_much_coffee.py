command = input()
cups_of_coffee = 0

while not command == "END":
    if command.lower() in "coding dog cat movie":
        if command.islower():
            cups_of_coffee += 1
        elif command.isupper():
            cups_of_coffee += 2
    command = input()

if cups_of_coffee <= 5:
    print(cups_of_coffee)
else:
    print('You need extra sleep')