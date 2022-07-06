command = input()
phone_book = {}

while "-" in command:
    name, phone_number = command.split("-")
    phone_book[name] = phone_number

    command = input()

number_of_searches = int(command)

for search in range(number_of_searches):
    searched_name = input()
    if searched_name in phone_book:
        print(f"{searched_name} -> {phone_book[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
