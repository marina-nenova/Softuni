fires = input().split("#")
available_water = int(input())
effort = 0
total_fire_extinguished = 0
fires_cells_extinguished = []

for fire_cell in fires:
    current_fire = fire_cell.split(" = ")
    fire_level = current_fire[0]
    cell_value = int(current_fire[1])
    if fire_level == "High":
        if not 81 <= cell_value <= 125:
            continue
    elif fire_level == "Medium":
        if not 51 <= cell_value <= 80:
            continue
    elif fire_level == "Low":
        if not 1 <= cell_value <= 50:
            continue
    if available_water < cell_value:
        continue

    fires_cells_extinguished.append(cell_value)
    available_water -= cell_value
    total_fire_extinguished += cell_value
    effort += cell_value * 0.25

print("Cells:")

for cell in fires_cells_extinguished:
    print(f" - {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire_extinguished}")
