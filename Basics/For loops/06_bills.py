time_period = int(input())
electicity_total = 0
water_total = 0
internet_total = 0
others_total = 0

for month in range(time_period):
    electricity_bill = float(input())
    electicity_total += electricity_bill
    water_total += 20
    internet_total += 15
    others_total += ((electricity_bill + 20 + 15) * 0.2) + electricity_bill + 20 + 15
average = (electicity_total + water_total + internet_total + others_total) / time_period

print(f"Electricity: {electicity_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {internet_total:.2f} lv")
print(f"Other: {others_total:.2f} lv")
print(f"Average: {average:.2f} lv")