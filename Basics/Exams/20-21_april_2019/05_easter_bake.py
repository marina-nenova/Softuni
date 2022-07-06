from math import ceil
number_of_easter_breads = int(input())
one_pack_sugar = 950
one_pack_flour = 750
total_sugar_used = 0
total_flour_used = 0
max_sugar_used = 0
max_flour_used = 0
for easter_bread in range(number_of_easter_breads):
    sugar_used = int(input())
    flour_used = int(input())
    total_sugar_used += sugar_used
    total_flour_used += flour_used
    if sugar_used > max_sugar_used:
        max_sugar_used = sugar_used
    if flour_used > max_flour_used:
        max_flour_used = flour_used

packs_sugar = ceil(total_sugar_used / one_pack_sugar)
packs_flour = ceil(total_flour_used / one_pack_flour)

print(f"Sugar: {packs_sugar}")
print(f"Flour: {packs_flour}")
print(f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")