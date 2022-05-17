from collections import deque

cups = deque([int(el) for el in input().split()])
bottles = [int(el) for el in input().split()]
wasted_water = 0

while True:
    if not cups:
        print(f"Bottles: {' '.join([str(bottles[index]) for index in range(len(bottles) -1, -1, -1)])}")
        break
    elif not bottles:
        print(f"Cups: {' '.join([str(el) for el in cups])}")
        break
    else:
        current_bottle = bottles.pop()
        cups[0] -= current_bottle
        if cups[0] <= 0:
            wasted_water += abs(cups.popleft())

print(f"Wasted litters of water: {wasted_water}")
