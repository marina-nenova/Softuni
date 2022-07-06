n = int(input())
combinations = 0
for x in range(n + 1):
    for y in range(n + 1):
        for z in range(n + 1):
            if x + y + z == n:
                combinations += 1
print(combinations)