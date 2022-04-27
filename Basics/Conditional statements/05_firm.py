import math

needed_hours = int(input())
days = int(input())
overtime_workers = int(input())

working_hours = (days - days * 0.1) * 8
overtime_hours = overtime_workers * (2 * days)

total_working_hours = math.floor(working_hours + overtime_hours)

if total_working_hours >= needed_hours:
    hours_left = total_working_hours - needed_hours
    print(f"Yes!{hours_left} hours left.")
else:
    hours_needed = needed_hours - total_working_hours
    print(f"Not enough time!{hours_needed} hours needed.")