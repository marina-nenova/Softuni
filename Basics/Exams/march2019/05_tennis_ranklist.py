from math import floor

number_of_tournaments = int(input())
starting_points = int(input())
points_from_tournaments = 0
tournaments_won = 0
for tournament in range(number_of_tournaments):
    stage_reached = input()
    if stage_reached == "W":
        points_from_tournaments += 2000
        tournaments_won +=1
    elif stage_reached == "F":
        points_from_tournaments += 1200
    elif stage_reached == "SF":
        points_from_tournaments += 720

total_points = points_from_tournaments + starting_points
average_points = floor(points_from_tournaments / number_of_tournaments)
tournaments_won_percentage = (tournaments_won / number_of_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{tournaments_won_percentage:.2f}%")