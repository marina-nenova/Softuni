from collections import deque

food_quantity = int(input())
orders = deque(int(el) for el in input().split())
print(max(orders))

while orders:
    if food_quantity >= orders[0]:
        food_quantity -= orders[0]
        orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")
else:
    orders = [str(num) for num in orders]
    print(f"Orders left: {' '.join(orders)}")
