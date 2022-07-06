number_of_frames = int(input())
type_of_frames = input()
type_of_delivery = input()
price_per_frame = 0
discount = 0

if type_of_frames == "90X130":
    price_per_frame = 110
    if 30 < number_of_frames <= 60:
        discount = 0.05
    elif number_of_frames > 60:
        discount = 0.08
elif type_of_frames == "100X150":
    price_per_frame = 140
    if 40 < number_of_frames <= 80:
        discount = 0.06
    elif number_of_frames > 80:
        discount = 0.1
elif type_of_frames == "130X180":
    price_per_frame = 190
    if 20 < number_of_frames <= 50:
        discount = 0.07
    elif number_of_frames > 50:
        discount = 0.12
elif type_of_frames == "200X300":
    price_per_frame = 250
    if 25 < number_of_frames <= 50:
        discount = 0.09
    elif number_of_frames > 50:
        discount = 0.14


total = number_of_frames * price_per_frame
total_after_discount = total - (total * discount)
final_total = 0
if type_of_delivery == "With delivery":
    final_total = total_after_discount + 60
elif type_of_delivery == "Without delivery":
    final_total = total_after_discount

if number_of_frames > 99:
    final_total -= final_total * 0.04

if number_of_frames > 10:
    print(f"{final_total:.2f} BGN")
else:
    print("Invalid order")
