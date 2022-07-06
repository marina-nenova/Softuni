def index_is_valid(index):
    if 0 <= index < len(message):
        return True
    return False


message = input()

command= input()

while not command == "Finish":
    data = command.split()
    action = data[0]

    if action == "Replace":
        current_char = data[1]
        new_char = data[2]
        message = message.replace(current_char, new_char)
        print(message)
    elif action == "Cut":
        start_index = int(data[1])
        end_index = int(data[2])
        if index_is_valid(start_index) and index_is_valid(end_index):
            message = message[:start_index] + message[end_index + 1:]
            print(message)
        else:
            print("Invalid indices!")

    elif action == "Make":
        modification = data[1]
        if modification == "Upper":
            message = message.upper()
        elif modification == "Lower":
            message = message.lower()
        print(message)

    elif action == "Check":
        substring = data[1]
        if substring in message:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")

    elif action == "Sum":
        start_index = int(data[1])
        end_index = int(data[2])
        if index_is_valid(start_index) and index_is_valid(end_index):
            substring = message[start_index: end_index + 1]
            sum_values = sum(ord(el) for el in substring)
            print(sum_values)
        else:
            print("Invalid indices!")
    command = input()
