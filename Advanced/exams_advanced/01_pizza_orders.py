from collections import deque

pizza_orders = deque([int(el) for el in input().split(", ")])
employees = [int(el) for el in input().split(", ")]
total_pizzas_made = 0

while pizza_orders and employees:
    current_order = pizza_orders.popleft()
    current_employee = employees.pop()

    if current_order <= 0:
        employees.append(current_employee)
        continue

    if current_order > 10:
        employees.append(current_employee)
        continue

    if current_order <= current_employee:
        total_pizzas_made += current_order
    else:
        total_pizzas_made += current_employee
        current_order -= current_employee
        pizza_orders.appendleft(current_order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f"Employees: {', '.join([str(el) for el in employees])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in pizza_orders])}")
