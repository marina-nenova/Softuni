password = input()
command = input()

while not command == "Done":
    data = command.split()
    action = data[0]

    if action == "TakeOdd":
        odd_chars = [ch for index, ch in enumerate(password) if index % 2 != 0]
        password = "".join(odd_chars)
        print(password)

    elif action == "Cut":
        index = int(data[1])
        length = int(data[2])
        substring = password[index: index + length]
        password = password.replace(substring, "", 1)
        print(password)

    elif action == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")
