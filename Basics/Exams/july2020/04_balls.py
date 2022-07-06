import math

number_of_balls = int(input())
other_colors_picked = 0
divides_from_black_balls = 0
number_of_red_balls = 0
number_of_orange_balls = 0
number_of_yellow_balls = 0
number_of_white_balls = 0
total_points = 0

for ball in range(number_of_balls):
    ball_color = input()
    if ball_color == "red":
        total_points += 5
        number_of_red_balls += 1
    elif ball_color == "orange":
        total_points += 10
        number_of_orange_balls += 1
    elif ball_color == "yellow":
        number_of_yellow_balls += 1
        total_points += 15
    elif ball_color == "white":
        number_of_white_balls += 1
        total_points += 20
    elif ball_color == "black":
        divides_from_black_balls += 1
        total_points /= 2
        total_points = math.floor(total_points)
    else:
        other_colors_picked += 1

print(f"Total points: {total_points}")
print(f"Red balls: {number_of_red_balls}")
print(f"Orange balls: {number_of_orange_balls}")
print(f"Yellow balls: {number_of_yellow_balls}")
print(f"White balls: {number_of_white_balls}")
print(f"Other colors picked: {other_colors_picked}")
print(f"Divides from black balls: {divides_from_black_balls}")
