rest_days = int(input())
work_days = 365 - rest_days
play_time = (work_days * 63 + rest_days * 127)

if play_time > 30000:
    overtime = play_time - 30000
    hours = overtime // 60
    minutes = overtime % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    time_left = 30000 - play_time
    hours = time_left // 60
    minutes = time_left % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")