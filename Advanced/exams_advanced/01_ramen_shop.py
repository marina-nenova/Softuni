from collections import deque

ramen_bowls = [int(el) for el in input().split(", ")]
customers = deque([int(el) for el in input().split(", ")])

while customers and ramen_bowls:
    current_bowl = ramen_bowls.pop()
    current_customer = customers.popleft()
    if current_bowl == current_customer:
        continue
    if current_bowl > current_customer:
        ramen_bowls.append(current_bowl - current_customer)
        continue
    else:
        customers.appendleft(current_customer - current_bowl)
        continue

if not customers:
    print("Great job! You served all the customers.")
else:
    print("Out of ramen! You didn't manage to serve all customers.")

if ramen_bowls:
    print(f"Bowls of ramen left: {', '.join([str(el) for el in ramen_bowls])}")
if customers:
    print(f"Customers left: {', '.join([str(el) for el in customers])}")