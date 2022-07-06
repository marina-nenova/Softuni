number_of_groups = int(input())
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0

for i in range(number_of_groups):
    people_per_group = int(input())
    if people_per_group <= 5:
        musala += people_per_group
    elif 6 <= people_per_group <= 12:
        monblan += people_per_group
    elif 13 <= people_per_group <= 25:
        kilimanjaro += people_per_group
    elif 26 <= people_per_group <= 40:
        k2 += people_per_group
    elif people_per_group >= 41:
        everest += people_per_group
    total_people += people_per_group
musala_percent = (musala / total_people) * 100
monblan_percent = (monblan / total_people) * 100
kilimanjaro_percent = (kilimanjaro / total_people) * 100
k2_percent = (k2 / total_people) * 100
everest_percent = (everest / total_people) * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")


