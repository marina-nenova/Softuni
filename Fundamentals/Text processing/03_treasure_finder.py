key = [int(el) for el in input().split()]
command = input()

key_index = 0

while not command == "find":
    message = command
    secret_message = ""
    treasure_type = ""
    location = ""

    for char in message:
        converted_char = chr(ord(char) - key[key_index])
        secret_message += converted_char
        key_index += 1
        if key_index > len(key) - 1:
            key_index = 0

    key_index = 0
    type_start = secret_message.index("&")
    type_end = secret_message.rindex("&")
    coordinates_start = secret_message.index("<")
    coordinates_end = secret_message.index(">")
    treasure_type = secret_message[type_start + 1: type_end]
    location = secret_message[coordinates_start + 1: coordinates_end]

    print(f"Found {treasure_type} at {location}")
    command = input()
    