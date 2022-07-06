text = input()
text_lower = text.lower()

sand_counter = text_lower.count("sand")
water_counter = text_lower.count("water")
fish_counter = text_lower.count("fish")
sun_counter = text_lower.count("sun")

total_counter = sand_counter + water_counter + fish_counter + sun_counter
print(total_counter)