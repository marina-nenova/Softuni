command = input()
tax = 0.2
taxes = 0
price_without_taxes = 0

while command not in "special regular":
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        price_without_taxes += price
        taxes += price * tax
    command = input()

total_price = price_without_taxes + taxes

if total_price == 0:
    print("Invalid order!")
else:
    if command == "special":
        total_price -= total_price * 0.1
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
