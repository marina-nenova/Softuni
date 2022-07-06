from collections import deque


def convert_str_to_seconds(time):
    hour, minutes, seconds = [int(x) for x in time.split(":")]
    time_in_sec = hour * 60 * 60 + minutes * 60 + seconds
    return time_in_sec

def convert_seconds_to_time(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots = input().split(";")
process_time_by_robot = {}
busy_until_by_robot = {}

for robot in robots:
    name, processing_time = robot.split("-")
    process_time_by_robot[name] = int(processing_time)
    busy_until_by_robot[name] = -1

time = convert_str_to_seconds(input())

command = input()
items = deque()

while not command == "End":
    product = command
    items.append(product)
    command = input()

while items:
    time += 1
    item = items.popleft()
    for name, busy_until in busy_until_by_robot.items():
        if time >= busy_until:
            busy_until_by_robot[name] = time + process_time_by_robot[name]
            print(f"{name} - {item} [{convert_seconds_to_time(time)}]")
            break
    else:
        items.append(item)
