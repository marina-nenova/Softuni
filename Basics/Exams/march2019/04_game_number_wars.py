first_player = input()
second_player = input()

command = input()
first_player_points = 0
second_player_points = 0
number_wars = False
first_player_won = False
second_player_won = False
while command != "End of game":
    first_player_card = int(command)
    second_player_card = int(input())
    difference = abs(first_player_card - second_player_card)
    if first_player_card > second_player_card:
        first_player_points += difference
    elif second_player_card > first_player_card:
        second_player_points += difference
    else:
        number_wars = True
        first_player_card = int(input())
        second_player_card = int(input())
        if first_player_card > second_player_card:
            first_player_won = True
        elif second_player_card > first_player_card:
            second_player_won = True
        break
    command = input()
if number_wars:
    print("Number wars!")
    if first_player_won:
        print(f"{first_player} is winner with {first_player_points} points")
    elif second_player_won:
        print(f"{second_player} is winner with {second_player_points} points")
else:
    print(f"{first_player} has {first_player_points} points")
    print(f"{second_player} has {second_player_points} points")