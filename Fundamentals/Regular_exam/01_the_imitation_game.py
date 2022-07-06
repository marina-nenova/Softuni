message = input()
command= input()

while not command == "Decode":
    data = command.split('|')
    action = data[0]

    if action == "Move":
        num = int(data[1])
        message = message[num:] + message[:num]

    elif action == "Insert":
        index = int(data[1])
        substring = data[2]
        message = message[:index] + substring + message[index:]

    elif action == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")
