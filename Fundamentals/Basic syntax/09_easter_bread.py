budget = float(input())
price_per_flour = float(input())

price_per_pack_of_eggs = price_per_flour * 0.75
price_per_l_of_milk = price_per_flour + (price_per_flour * 0.25)

price_per_loaf = price_per_pack_of_eggs + price_per_flour + (price_per_l_of_milk / 4)
bread_count = 0
egg_count = 0
while budget > price_per_loaf:
    bread_count += 1
    egg_count += 3
    if bread_count % 3 == 0:
        egg_count -= bread_count - 2
    budget -= price_per_loaf

print(f"You made {bread_count} loaves of Easter bread! Now you have {egg_count} eggs and {budget:.2f}BGN left.")