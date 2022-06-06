import os

command = input()

while not command == "End":
    data = command.split("-")
    action = data[0]
    file_name = data[1]

    if action == "Create":
        open(file_name, "w").close()

    elif action == "Add":
        content = data[2]
        with open(file_name, "a") as file:
            file.write(f"{content}\n")

    elif action == "Replace":
        old_string = data[2]
        new_string = data[3]
        try:
            with open(file_name, "r+") as file:
                new_text = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(new_text)
        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

    command = input()