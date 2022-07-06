number_of_groups = int(input())
hikers_on_musala = 0
hikers_on_monblan = 0
hikers_on_kilimanjaro = 0
hikers_on_k2 = 0
hikers_on_everest = 0
total_hikers = 0

for group in range(number_of_groups):
    people_per_group = int(input())
    total_hikers += people_per_group
    if people_per_group <= 5:
        hikers_on_musala += people_per_group
    elif 6 <= people_per_group <= 12:
        hikers_on_monblan += people_per_group
    elif 13 <= people_per_group <= 25:
        hikers_on_kilimanjaro += people_per_group
    elif 26 <= people_per_group <= 40:
        hikers_on_k2 += people_per_group
    else:
        hikers_on_everest += people_per_group
going_to_musala = (hikers_on_musala / total_hikers) * 100
going_to_monblan = (hikers_on_monblan / total_hikers) * 100
going_to_kilimanjaro = (hikers_on_kilimanjaro / total_hikers) * 100
going_to_k2 = (hikers_on_k2 / total_hikers) * 100
going_to_everest = (hikers_on_everest / total_hikers) * 100

print(f"{going_to_musala:.2f}%")
print(f"{going_to_monblan:.2f}%")
print(f"{going_to_kilimanjaro:.2f}%")
print(f"{going_to_k2:.2f}%")
print(f"{going_to_everest:.2f}%")


