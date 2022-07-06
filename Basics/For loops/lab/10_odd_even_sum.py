n = int(input())

even_total = 0
odd_total = 0
for i in range(1, n + 1):
    number = int(input())
    if i % 2 == 0:
        even_total += number
    else:
        odd_total += number

if even_total == odd_total:
    print("Yes")
    print(f"Sum = {even_total}")
else:
    difference = abs(even_total - odd_total)
    print("No")
    print(f"Diff = {difference}")

