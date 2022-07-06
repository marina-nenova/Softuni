bottles_of_detergent = int(input())
total_detergent = bottles_of_detergent * 750
clean_dishes = 0
clean_pots = 0
counter = 0

while total_detergent >= 0:
    counter += 1
    number_of_dishes = input()
    if number_of_dishes == "End":
        print("Detergent was enough!")
        print(f"{clean_dishes} dishes and {clean_pots} pots were washed.")
        print(f"Leftover detergent {total_detergent} ml.")
        break

    if counter % 3 == 0:
        clean_pots += int(number_of_dishes)
        total_detergent -= int(number_of_dishes) * 15
    else:
        clean_dishes += int(number_of_dishes)
        total_detergent -= int(number_of_dishes) * 5

if total_detergent < 0:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
