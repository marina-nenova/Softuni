venue_rent = float(input())

cake_price = venue_rent * 0.2
drinks = cake_price - (cake_price * 0.45)
animation = venue_rent / 3

needed_budget = venue_rent + cake_price + drinks + animation
print(f"{needed_budget:.1f}")