country = input()
category = input()

difficulty = 0
performance = 0

if country == "Russia":
    if category == "ribbon":
        difficulty = 9.100
        performance = 9.400
    elif category == "hoop":
        difficulty = 9.300
        performance = 9.800
    elif category == "rope":
        difficulty = 9.600
        performance = 9.000
if country == "Bulgaria":
    if category == "ribbon":
        difficulty = 9.600
        performance = 9.400
    elif category == "hoop":
        difficulty = 9.550
        performance = 9.750
    elif category == "rope":
        difficulty = 9.500
        performance = 9.400
if country == "Italy":
    if category == "ribbon":
        difficulty = 9.200
        performance = 9.500
    elif category == "hoop":
        difficulty = 9.450
        performance = 9.350
    elif category == "rope":
        difficulty = 9.700
        performance = 9.150
max_points = 20
total_per_category = difficulty + performance
points_to_max = 20 - total_per_category
percentage = (points_to_max / 20) * 100

print(f"The team of {country} get {total_per_category:.3f} on {category}.")
print(f"{percentage:.2f}%")