fruit_content = input()
type_of_pack = input()
ordered_packs = int(input())

price_per_pack = 0

if fruit_content == "Watermelon":
    if type_of_pack == "small":
        price_per_pack = 56 * 2
    elif type_of_pack == "big":
        price_per_pack = 28.7 * 5
elif fruit_content == "Mango":
    if type_of_pack == "small":
        price_per_pack = 36.66 * 2
    elif type_of_pack == "big":
        price_per_pack = 19.6 * 5
elif fruit_content == "Pineapple":
    if type_of_pack == "small":
        price_per_pack = 42.1 * 2
    elif type_of_pack == "big":
        price_per_pack = 24.8 * 5
elif fruit_content == "Raspberry":
    if type_of_pack == "small":
        price_per_pack = 20 * 2
    elif type_of_pack == "big":
        price_per_pack = 15.2 * 5

total_price = price_per_pack * ordered_packs

if 400 <= total_price <= 1000:
    total_price -= total_price * 0.15
elif total_price > 1000:
    total_price -= total_price * 0.5

print(f"{total_price:.2f} lv.")