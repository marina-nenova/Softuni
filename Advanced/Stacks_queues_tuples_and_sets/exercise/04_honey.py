from collections import deque

bees = deque([int(el) for el in input().split()])
nectar = [int(el) for el in input().split()]
operation_symbols = deque(input().split())
total_honey = 0

while bees and nectar:
    current_bee = bees[0]
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        bees.popleft()
        operator = operation_symbols.popleft()
        if operator == "+":
            total_honey += abs(current_bee + current_nectar)
        if operator == "-":
            total_honey += abs(current_bee - current_nectar)
        if operator == "*":
            total_honey += abs(current_bee * current_nectar)
        if operator == "/" and current_nectar > 0:
            total_honey += abs(current_bee / current_nectar)

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(el) for el in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(el) for el in nectar)}")
