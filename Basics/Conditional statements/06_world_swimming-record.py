import math

world_record = float(input())
distance = float(input())
second_per_one_meter = float(input())

time_needed = distance * second_per_one_meter
time_added = math.floor(distance / 15) * 12.5
total_time = time_needed + time_added

if total_time < world_record:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    seconds_needed = total_time - world_record
    print(f"No, he failed! He was {seconds_needed:.2f} seconds slower.")