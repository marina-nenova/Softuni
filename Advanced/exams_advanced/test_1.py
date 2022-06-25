from collections import deque

a = deque([int(el) for el in input().split(", ")])
b = [int(el) for el in input().split(", ")]

while a and b:
    current_a = a.popleft()
    current_b = b.pop()

    if current_b <= 0 and current_a <= 0:
        continue

    if current_a <= 0:
        b.append(current_b)
        continue

    if current_b <= 0:
        a.appendleft(current_a)
        continue