
change = float(input())
left = int(change * 100)
coins = 0

while left > 0:
    if left >= 200:
        coins += left // 200
        left = left % 200
    elif left >= 100:
        coins += 1
        left = left % 100
    elif left >= 50:
        coins += 1
        left = left % 50
    elif left >= 20:
        coins += left // 20
        left = left % 20
    elif left >= 10:
        coins += 1
        left = left % 10
    elif left >= 5:
        coins += 1
        left = left % 5
    elif left >= 2:
        coins += left // 2
        left = left % 2
    elif left >= 1:
        coins += 1
        left = left % 1
if change == 0:
    coins = 0
print(coins)