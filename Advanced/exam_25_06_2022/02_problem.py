player_1, player_2 = input().split(", ")
size = 6

maze = [input().split() for _ in range(size)]

current_player, next_player = player_1, player_2
player_skips = {"Tom": False, "Jerry": False}

while True:
    player_row, player_col = eval(input())

    if not player_skips[current_player]:
        if maze[player_row][player_col] == "E":
            print(f"{current_player} found the Exit and wins the game!")
            break
        elif maze[player_row][player_col] == "T":
            print(f"{current_player} is out of the game! The winner is {next_player}.")
            break
        elif maze[player_row][player_col] == "W":
            print(f"{current_player} hits a wall and needs to rest.")
            player_skips[current_player] = True
    else:
        player_skips[current_player] = False

    current_player, next_player = next_player, current_player
