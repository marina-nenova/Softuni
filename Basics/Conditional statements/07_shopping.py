budget = float(input())
video_cards = int(input())
cpu = int(input())
ram = int(input())

video_card_total = video_cards * 250
cpu_total = (video_card_total * 0.35) * cpu
ram_total = (video_card_total * 0.1) * ram

total = video_card_total + cpu_total + ram_total

if video_cards > cpu:
    total = total - total * 0.15

if budget >= total:
    money_left = budget - total
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed = total - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")


