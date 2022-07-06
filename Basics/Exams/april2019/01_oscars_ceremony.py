hall_rent = int(input())

awards = hall_rent - (hall_rent * 0.3)
catering = awards - (awards * 0.15)
sound = catering / 2

total_expences = awards + catering + sound + hall_rent

print(f"{total_expences:.2f}")