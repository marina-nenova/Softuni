neighbourhood = [int(el) for el in input().split("@")]

command = input()
last_position = 0
while not command == "Love!":
    action = command.split()
    length = int(action[1])
    curren_position = last_position + length
    if curren_position > len(neighbourhood) - 1:
        curren_position = 0
    if neighbourhood[curren_position] > 0:
        neighbourhood[curren_position] -= 2
        if neighbourhood[curren_position] == 0:
            print(f"Place {curren_position} has Valentine's day.")
    else:
        print(f"Place {curren_position} already had Valentine's day.")
    last_position = curren_position
    cupid_last_position = last_position
    command = input()
print(f"Cupid's last position was {last_position}.")

count_of_no_valentines = len([el for el in neighbourhood if el != 0])
if count_of_no_valentines == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count_of_no_valentines} places.")