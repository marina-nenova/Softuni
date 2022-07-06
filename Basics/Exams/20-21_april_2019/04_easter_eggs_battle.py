eggs_per_player_one = int(input())
eggs_per_player_two = int(input())
player_one_lost = False
player_two_lost = False
command = input()

while command != "End of battle":
    winner = command
    if winner == "one":
        eggs_per_player_two -= 1
    elif winner == "two":
        eggs_per_player_one -= 1
    if eggs_per_player_one == 0:
        player_one_lost = True
        break
    elif eggs_per_player_two == 0:
        player_two_lost = True
        break
    command = input()

if player_one_lost:
    print(f"Player one is out of eggs. Player two has {eggs_per_player_two} eggs left.")
elif player_two_lost:
    print(f"Player two is out of eggs. Player one has {eggs_per_player_one} eggs left.")
else:
    print(f"Player one has {eggs_per_player_one} eggs left.")
    print(f"Player two has {eggs_per_player_two} eggs left.")