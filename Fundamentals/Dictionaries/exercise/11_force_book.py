def user_exists(user):
    for user_names in force_book.values():
        if user in user_names:
            return True
    return False


def remove_user(user):
    for user_names in force_book.values():
        if user in user_names:
            user_names.remove(user)


command = input()
force_book = {}

while not command == "Lumpawaroo":
    if "|" in command:
        force_side, user_name = command.split(" | ")
        if force_side not in force_book:
            force_book[force_side] = []
        if not user_exists(user_name):
            force_book[force_side].append(user_name)

    elif " -> " in command:
        user_name, force_side = command.split(" -> ")
        if user_exists(user_name):
            remove_user(user_name)
        if force_side not in force_book:
            force_book[force_side] = []

        force_book[force_side].append(user_name)
        print(f"{user_name} joins the {force_side} side!")

    command = input()

for side, users in force_book.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
