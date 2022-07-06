target_minutes = int(input())
target_seconds = int(input())
track_length = float(input())
seconds_per_100_meters = int(input())

target_time_in_seconds = (target_minutes * 60) + target_seconds
slowing_time = (track_length / 120) * 2.5
martin_time = (track_length / 100) * seconds_per_100_meters - slowing_time

if martin_time <= target_time_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {martin_time:.3f}.")
else:
    needed_seconds = martin_time - target_time_in_seconds
    print(f"No, Marin failed! He was {needed_seconds:.3f} second slower.")