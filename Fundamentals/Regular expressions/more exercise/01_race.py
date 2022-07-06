import re

name_pattern = r"[A-Za-z]"
distance_pattern = r"\d"
racers = input().split(", ")
text = input()
race_info = {}

while not text == "end of race":
    racer_name = "".join(re.findall(name_pattern, text))
    distance = sum([int(num) for num in re.findall(distance_pattern, text)])

    if racer_name in racers:
        if racer_name not in race_info:
            race_info[racer_name] = distance
        else:
            race_info[racer_name] += distance

    text = input()

sorted_dict = dict(sorted(race_info.items(), key=lambda x: -x[1]))
racer_info = [key for key in sorted_dict]

places = ["1st", "2nd", "3rd"]
for i in range(len(places)):
    print(f"{places[i]} place: {racer_info[i]}")
