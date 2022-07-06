strawberries_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - (raspberries_price * 0.4)
bananas_price = raspberries_price - (raspberries_price * 0.8)

total = strawberries * strawberries_price + bananas * bananas_price + raspberries * raspberries_price + oranges * oranges_price
print(f"{total:.2f}")