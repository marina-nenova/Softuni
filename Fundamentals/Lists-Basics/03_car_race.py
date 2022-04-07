numbers = [int(el) for el in input().split()]

middle = int(len(numbers)/2)
left_racer = numbers[:middle]
right_racer = numbers[middle + 1:]
right_racer_time = 0
left_racer_time = 0

for index in range(len(left_racer)):
    time = left_racer[index]
    left_racer_time += time
    if time == 0:
        left_racer_time *= 0.8
for index in range(len(right_racer)-1, -1, -1):
    time = right_racer[index]
    right_racer_time += time
    if time == 0:
        right_racer_time *= 0.8

winner = ""
winner_time = 0
if left_racer_time < right_racer_time:
    winner = "left"
    winner_time = left_racer_time
else:
    winner = "right"
    winner_time = right_racer_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")