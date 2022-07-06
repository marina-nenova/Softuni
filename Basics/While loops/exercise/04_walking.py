steps_goal = 10000
steps_walked = 0

while steps_walked < steps_goal:
    steps_per_day = input()
    if steps_per_day == "Going home":
        steps_walked_home = int(input())
        steps_walked += steps_walked_home
        break
    else:
        steps_walked += int(steps_per_day)
difference = abs(steps_walked - steps_goal)
if steps_walked >= steps_goal:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")


