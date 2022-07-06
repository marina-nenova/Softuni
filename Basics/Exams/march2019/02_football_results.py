first_game_result = input()
second_game_result = input()
third_game_result = input()

games_won = 0
games_lost = 0
games_draw = 0
if int(first_game_result[0]) > int(first_game_result[2]):
    games_won += 1
elif int(first_game_result[0]) < int(first_game_result[2]):
    games_lost += 1
elif int(first_game_result[0]) == int(first_game_result[2]):
    games_draw += 1
if int(second_game_result[0]) > int(second_game_result[2]):
    games_won += 1
elif int(second_game_result[0]) < int(second_game_result[2]):
    games_lost += 1
elif int(second_game_result[0]) == int(second_game_result[2]):
    games_draw += 1
if int(third_game_result[0]) > int(third_game_result[2]):
    games_won += 1
elif int(third_game_result[0]) < int(third_game_result[2]):
    games_lost += 1
elif int(third_game_result[0]) == int(third_game_result[2]):
    games_draw += 1

print(f"Team won {games_won} games.")
print(f"Team lost {games_lost} games.")
print(f" Drawn games: {games_draw}")