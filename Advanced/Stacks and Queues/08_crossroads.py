from collections import deque

green_light = int(input())
window = int(input())

command = input()
cars_line = deque()
cars_counter = 0
crash_happened = False
while not command == "END":

    if command == "green":
        if cars_line:
            current_car = cars_line.popleft()
            time_to_pass = green_light - len(current_car)
            while time_to_pass > 0:
                cars_counter += 1
                if cars_line:
                    current_car = cars_line.popleft()
                    time_to_pass -= len(current_car)
                else:
                    break

            if time_to_pass == 0:
                cars_counter += 1

            elif time_to_pass < 0:
                if window >= abs(time_to_pass):
                    cars_counter += 1
                else:
                    index = window + time_to_pass
                    print("A crash happened!")
                    print(f"{current_car} was hit at {current_car[index]}.")
                    crash_happened = True
                    break
    else:
        cars_line.append(command)
    command = input()

if not crash_happened:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")
