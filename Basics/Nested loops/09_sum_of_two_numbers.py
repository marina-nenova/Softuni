start = int(input())
stop = int(input())
magic_number = int(input())
total = 0
counter = 0
combination_found = False
for i in range(start, stop + 1):
    for j in range(start, stop + 1):
        total = i + j
        counter += 1
        if total == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            combination_found = True
            break
    if combination_found:
        break
if not combination_found:
    print(f"{counter} combinations - neither equals {magic_number}")
