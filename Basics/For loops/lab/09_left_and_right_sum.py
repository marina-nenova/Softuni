n = int(input())
total1 = 0
for _ in range(n):
    number1 = int(input())
    total1 += number1
total2 = 0
for _ in range(n):
    number2 = int(input())
    total2 += number2

if total1 == total2:
    print(f"Yes, sum = {total1}")

else:
    difference = abs(total1 - total2)
    print(f"No, diff = {difference}")

