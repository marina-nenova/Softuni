number_of_trainees = int(input())

back_training = 0
chest_training = 0
legs_training = 0
abs_training = 0
protein_shakes_bought = 0
protein_bar_bought = 0

for trainee in range(number_of_trainees):
    activity = input()
    if activity == "Back":
        back_training += 1
    elif activity == "Chest":
        chest_training += 1
    elif activity == "Legs":
        legs_training += 1
    elif activity == "Abs":
        abs_training += 1
    elif activity == "Protein shake":
        protein_shakes_bought += 1
    elif activity == "Protein bar":
        protein_bar_bought += 1

people_training = back_training + chest_training + legs_training + abs_training
people_buying = protein_shakes_bought + protein_bar_bought

people_training_percentage = (people_training / number_of_trainees) * 100
people_buying_percentage = (people_buying / number_of_trainees) * 100

print(f"{back_training} - back")
print(f"{chest_training} - chest")
print(f"{legs_training} - legs")
print(f"{abs_training} - abs")
print(f"{protein_shakes_bought} - protein shake")
print(f"{protein_bar_bought} - protein bar")
print(f"{people_training_percentage:.2f}% - work out")
print(f"{people_buying_percentage:.2f}% - protein")