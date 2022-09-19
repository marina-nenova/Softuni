vegetables_price = float(input())
fruits_price = float(input())
vegetables_quantity = int(input())
fruits_quantity = int(input())

total_in_lv = vegetables_quantity * vegetables_price + fruits_quantity * fruits_price
total_in_eur = total_in_lv / 1.94
print(f"{total_in_eur:.2f}")
