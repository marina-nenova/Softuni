from collections import deque

jobs = deque([int(el) for el in input().split(", ")])
target_index = int(input())
target_job = jobs[target_index]

cycles = 0

for idx in range(len(jobs)):
    current_job = jobs[idx]
    if current_job < target_job or (current_job == target_job and target_index >= idx):
        cycles += current_job

print(cycles)