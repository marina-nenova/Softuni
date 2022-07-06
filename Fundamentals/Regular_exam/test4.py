command = input()

guest_info = {}
unliked_meals = 0
while not command == "Stop":
    action, guest, meal = command.split("-")
    if action == "Like":
        if guest not in guest_info:
            guest_info[guest] = []
        if meal not in guest_info[guest]:
            guest_info[guest].append(meal)
    elif action == "Dislike":
        if guest not in guest_info:
            print(f"The {guest} is not at the party")
        elif meal not in guest_info[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            guest_info[guest].remove(meal)
            print(f"{guest} does not like the {meal}")
            unliked_meals += 1
    command = input()

for guest, info in guest_info.items():
    print(f"{guest}: {', '.join(info)}")

print(f"Unliked meals: {unliked_meals}")
