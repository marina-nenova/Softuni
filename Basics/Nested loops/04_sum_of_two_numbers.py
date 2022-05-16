n1 = int(input())
n2 = int(input())
magic_number = int(input())
counter = 0

condition = False

for x in range(n1, n2 +1):
    for y in range(n1, n2 + 1):
        counter += 1
        if x + y == magic_number:
            condition = True
            print(f"Combination N:{counter} ({x} + {y} = {magic_number})")
            break
    if condition:
        break
if not condition:
    print(f"{counter} combinations - neither equals {magic_number}")