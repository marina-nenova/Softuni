countries = input().split(", ")
capitals = input().split(", ")

countries_dict = dict(zip(countries, capitals))

for country, capital in countries_dict.items():
    print(f"{country} -> {capital}")
