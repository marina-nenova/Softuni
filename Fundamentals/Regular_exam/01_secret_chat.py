message = input()

command = input()

while not command == "Reveal":
    data = command.split(":|:")
    action = data[0]
    if action == "InsertSpace":
        index = int(data[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif action == "Reverse":
        substring = data[1]
        if substring in message:
            message = message.replace(substring, "", 1) + substring[::-1]
            print(message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)
        print(message)

    command = input()

print(f"You have a new text message: {message}")