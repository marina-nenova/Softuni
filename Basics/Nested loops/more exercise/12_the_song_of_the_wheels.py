control_number = int(input())
password = ""
counter = 0
is_found = False
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a < b and c > d) and (a * b + c * d == control_number):
                    print(f"{a}{b}{c}{d}", end = " ")
                    counter += 1
                    if counter == 4:
                        password = f"{a}{b}{c}{d}"
                        is_found = True
if is_found:
    print()
    print(f"Password: {password}")
else:
    print()
    print("No!")