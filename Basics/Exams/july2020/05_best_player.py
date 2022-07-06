import sys

name_of_player = input()
max_goals = 0
best_player = ""
while name_of_player != "END":
    number_of_goals = int(input())
    if number_of_goals > max_goals:
        max_goals = number_of_goals
        best_player = name_of_player
    if number_of_goals >= 10:
        break
    name_of_player = input()

print(f"{best_player} is the best player!")

if max_goals >= 3:
    print( f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")