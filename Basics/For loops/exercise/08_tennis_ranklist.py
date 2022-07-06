import math

number_of_tournaments = int(input())
initial_points = int(input())
points_from_tournaments = 0
number_of_wins = 0
for i in range(number_of_tournaments):
    tournament_status = input()
    if tournament_status == "W":
        points_from_tournaments += 2000
        number_of_wins += 1
    elif tournament_status == "F":
        points_from_tournaments += 1200
    elif tournament_status == "SF":
        points_from_tournaments += 720
total_points = points_from_tournaments + initial_points
average_points = points_from_tournaments / number_of_tournaments
wins_percentage = (number_of_wins / number_of_tournaments) * 100
print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{wins_percentage:.2f}%")
