import re

pattern = r"%(?P<name>[A-Z]{1}[a-z]+)%[^|$%.]*<(?P<product>[\w]+)>[^|$%.]*\|(?P<count>[\d]+)\|[^|$%.\d+]*(?P<price>[\d]+\.?[\d]+)\$"

text = input()
total_income = 0
while not text == "end of shift":
    valid_order = re.search(pattern, text)
    if valid_order is not None:
        name = valid_order.group("name")
        product = valid_order.group("product")
        total_price = int(valid_order.group("count")) * float(valid_order.group("price"))
        total_income += total_price
        print(f"{name}: {product} - {total_price:.2f}")

    text = input()

print(f"Total income: {total_income:.2f}")
