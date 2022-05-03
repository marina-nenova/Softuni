hour = int(input())
day_of_week = input()

if hour >= 10 and hour <= 18 and day_of_week != "Sunday":
    print("open")
else:
    print("closed")