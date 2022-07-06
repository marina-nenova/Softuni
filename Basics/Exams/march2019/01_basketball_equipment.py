training_annual_fee = int(input())

shoes_price = training_annual_fee - (training_annual_fee * 0.4)
clothes_price = shoes_price - (shoes_price * 0.2)
basketball_price = clothes_price / 4
accessories_price = basketball_price / 5

total_expenses = training_annual_fee + shoes_price + clothes_price + basketball_price + accessories_price

print(f"{total_expenses:.2f}")