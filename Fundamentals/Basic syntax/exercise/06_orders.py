number_of_orders = int(input())
total = 0

for order in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    order_price = days * capsules_count * price_per_capsule
    print(f"The price for the coffee is: ${order_price:.2f}")
    total += order_price
print(f"Total: ${total:.2f}")
