import math

record = float(input())
meters = float(input())
time_per_meter = float(input())

time_per_distance = meters * time_per_meter
slowing_time = math.floor(meters / 50) * 30
time_needed = time_per_distance + slowing_time

difference = abs(record - time_needed)
if time_needed < record:
    print(f" Yes! The new record is {time_needed:.2f} seconds.")
else:
    print(f"No! He was {difference:.2f} seconds slower.")