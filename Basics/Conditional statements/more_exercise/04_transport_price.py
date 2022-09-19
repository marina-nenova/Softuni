kilometers = int(input())
time_of_day = input()

taxi = 0
bus = 0.09 * kilometers
train = 0.06 * kilometers

if time_of_day == "day":
    taxi = 0.7 + (0.79 * kilometers)
elif time_of_day == "night":
    taxi = 0.7 + (0.9 * kilometers)

if kilometers < 20:
    print(f"{taxi:.2f}")
elif 20 <= kilometers < 100:
    print(f"{bus:.2f}")
else:
    print(f"{train:.2f}")
