houses = [int(num) for num in input().split("@")]

command = input()
previous_index = 0
last_position = 0
while not command == "Love!":
    action = command.split()
    length = int(action[1])
    current_index = previous_index + length
    if current_index > len(houses)-1:
        current_index = 0
    if houses[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        houses[current_index] -= 2
        if houses[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")
    previous_index = current_index
    last_position = current_index
    command = input()

final_houses = [num for num in houses if num > 0]
house_count = len(final_houses)

print(f"Cupid's last position was {last_position}.")
if house_count > 0:
    print(f"Cupid has failed {house_count} places.")
else:
    print("Mission was successful.")