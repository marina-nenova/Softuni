import math

series = input()
episode_length = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4
free_time = break_time - lunch_time - rest_time

if free_time >= episode_length:
    time_left = math.ceil(free_time - episode_length)
    print(f"You have enough time to watch {series} and left with {time_left} minutes free time.")
else:
    time_needed = math.ceil(episode_length - free_time)
    print(f"You don't have enough time to watch {series}, you need {time_needed} more minutes.")