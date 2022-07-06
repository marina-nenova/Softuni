from collections import deque

chocolates = [int(el) for el in input().split(", ")]
milk = deque([int(el) for el in input().split(", ")])

milkshakes_count = 0


while chocolates and milk and milkshakes_count < 5:
    chocolate = chocolates.pop()
    milk_cup = milk.popleft()
    if chocolate <= 0 and milk_cup <= 0:
        continue
    if chocolate <= 0:
        milk.appendleft(milk_cup)
        continue
    if milk_cup <= 0:
        chocolates.append(chocolate)
        continue
    if chocolate == milk_cup:
        milkshakes_count += 1
    else:
        milk.append(milk_cup)
        chocolates.append(chocolate - 5)

if milkshakes_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(el) for el in chocolates)}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(str(el) for el in milk)}")
else:
    print("Milk: empty")
