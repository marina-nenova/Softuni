activation_key = input()

command = input()

while not command == "Generate":
    data = command.split(">>>")
    action = data[0]

    if action == "Contains":
        substring = data[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        modification = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        substring = activation_key[start_index:end_index]
        if modification == "Upper":
            activation_key = activation_key[:start_index] + substring.upper() + activation_key[end_index:]
        elif modification == "Lower":
            activation_key = activation_key[:start_index] + substring.lower() + activation_key[end_index:]
        print(activation_key)

    elif action == "Slice":
        start_index = int(data[1])
        end_index = int(data[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")
