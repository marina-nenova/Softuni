days = int(input())
daily_loot = int(input())
expected_loot = float(input())
total_loot = 0

for day in range(1, days + 1):
    total_loot += daily_loot
    if day % 3 == 0:
        total_loot += daily_loot * 0.5
    if day % 5 == 0:
        total_loot -= total_loot * 0.3

if total_loot >= expected_loot:
    print(f"Ahoy! {total_loot:.2f} plunder gained.")
else:
    percentage = (total_loot / expected_loot) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")