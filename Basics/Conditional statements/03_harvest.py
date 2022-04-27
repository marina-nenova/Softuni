import math
square_meters = int(input())
grapes_per_sqm = float(input())
litres_needed = int(input())
workers = int(input())

total_grapes = square_meters * grapes_per_sqm
wine = (0.4 * total_grapes) / 2.5

if wine < litres_needed:
    needed = math.floor(litres_needed - wine)
    print(f"It will be a tough winter! More {needed} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    litres_left = math.ceil(wine - litres_needed)
    wine_per_worker = math.ceil(litres_left / workers)
    print(f"{litres_left} liters left -> {wine_per_worker} liters per person.")