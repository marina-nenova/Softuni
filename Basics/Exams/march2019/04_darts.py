player_name = input()

starting_points = 301
successful_shots = 0
unsuccessful_shots = 0
points_registered = 0
command = input()
leg_won = False
while command != "Retire":
    sector_hit = command
    points_hit = int(input())
    if sector_hit == "Single":
        points_registered = points_hit
    elif sector_hit == "Double":
        points_registered = points_hit * 2
    elif sector_hit == "Triple":
        points_registered = points_hit * 3
    if points_registered <= starting_points:
        successful_shots += 1
        starting_points -= points_registered
    else:
        unsuccessful_shots += 1
    if starting_points == 0:
        leg_won = True
        break
    command = input()
if leg_won:
    print(f"{player_name} won the leg with {successful_shots} shots.")
else:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")