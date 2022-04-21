num_chicken = int(input())
num_fish = int(input())
num_vegetarian = int(input())

total_menus = num_chicken * 10.35 + num_fish * 12.4 + num_vegetarian * 8.15
final_total = (total_menus + total_menus * 0.2) + 2.5

print(final_total)