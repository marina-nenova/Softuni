number = int(input())
bonus = 0
if number <= 100:
    bonus = 5
elif number > 1000:
    bonus = number * 0.1
else:
    bonus = number * 0.2

if number %2 == 0:
    bonus = bonus + 1
elif number %10 == 5:
    bonus = bonus + 2

total = number + bonus
print(bonus)
print(total)

