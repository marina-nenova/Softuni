hour = int(input())
minutes = int(input())

new_time = 0
new_minutes = 0
if minutes + 15 >= 60:
    new_time = hour + 1
    new_minutes = (minutes + 15) - 60
    if new_time >= 24:
        new_time = 0
else:
    new_time = hour
    new_minutes = minutes + 15

if new_minutes < 10:
    print(f"{new_time}:0{new_minutes}")
else:
    print(f"{new_time}:{new_minutes}")