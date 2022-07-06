actor_name = input()
academy_points = float(input())
number_of_judges = int(input())
judges_points = 0
total_points = academy_points
nomination = False
for judge in range(number_of_judges):
    name_of_judge = input()
    points_from_judge = float(input())
    total_points_from_judge = (len(name_of_judge) * points_from_judge) / 2
    total_points += total_points_from_judge
    if total_points > 1250.5:
        nomination = True
        break

if nomination:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    points_needed = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")