text = input()
total = 0

for ch in text:
    if ch == "a":
        total += 1
    elif ch == "e":
        total += 2
    elif ch == "i":
        total += 3
    elif ch == "o":
        total += 4
    elif ch == "u":
        total += 5

print(total)


