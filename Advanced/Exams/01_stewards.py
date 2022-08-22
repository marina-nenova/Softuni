from collections import deque

seats = input().split(', ')
first = deque(int(x) for x in input().split(', '))
last = deque(int(x) for x in input().split(', '))
rotations = 0
matches = []

while first and last:
    num1 = first.popleft()
    num2 = last.pop()
    symbol = chr(num1 + num2)
    rotations += 1

    seat1 = f"{num1}{symbol}"
    seat2 = f"{num2}{symbol}"

    if seat1 not in seats and seat2 not in seats:
        first.append(num1)
        last.appendleft(num2)

    if seat1 in seats and seat1 not in matches:
        matches.append(seat1)

    if seat2 in seats and seat2 not in matches:
        matches.append(seat2)

    if len(matches) == 3:
        break

    if rotations == 10:
        break

print(f"Seat matches: {', '.join(matches)}")
print(f"Rotations count: {rotations}")