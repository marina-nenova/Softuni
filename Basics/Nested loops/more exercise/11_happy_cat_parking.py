number_of_days = int(input())
number_of_hours = int(input())

total_sum = 0

for day in range(1, number_of_days + 1):
    hourly_sum = 0
    daily_sum = 0
    for hour in range(1, number_of_hours + 1):
        if (day % 2 == 0 and hour % 2 == 0) or (day % 2 == 1 and hour % 2 == 1):
            hourly_sum = 1
        elif day % 2 == 0 and hour % 2 == 1:
            hourly_sum = 2.5
        elif day % 2 == 1 and hour % 2 == 0:
            hourly_sum = 1.25
        daily_sum += hourly_sum
    print(f"Day: {day} - {daily_sum:.2f} leva")

    total_sum += daily_sum
print(f"Total: {total_sum:.2f} leva")