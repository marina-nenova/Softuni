easter_bread = int(input())
cartons_of_eggs = int(input())
bisquits = int(input())

easter_bread_price = 3.2
carton_of_eggs_price = 4.35
eggs_per_carton = 12
bisquts_price = 5.4
eggs_coloring_per_egg = 0.15

easter_bread_total = easter_bread * easter_bread_price
cartons_of_eggs_total = cartons_of_eggs * carton_of_eggs_price
bisquits_total = bisquits * bisquts_price
eggs_coloring_total = (cartons_of_eggs * eggs_per_carton) * eggs_coloring_per_egg

total_expenses = easter_bread_total + cartons_of_eggs_total + bisquits_total + eggs_coloring_total

print(f"{total_expenses:.2f}")

