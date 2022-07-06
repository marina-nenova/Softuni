hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())
time_of_exam = hour_of_exam * 60 + minutes_of_exam
time_of_arrival = hour_of_arrival * 60 + minute_of_arrival

if time_of_arrival > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print("On time")
else:
    print("Early")

difference = abs(time_of_arrival - time_of_exam)

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f"{difference} minutes before the start")

elif time_of_arrival <= time_of_exam - 60:
    hh = difference // 60
    mm = difference % 60
    if mm < 10:
        print(f"{hh}:0{mm} hours before the start")
    else:
        print(f"{hh}:{mm} hours before the start")
elif time_of_exam < time_of_arrival < time_of_exam + 60:
    print(f"{difference} minutes after the start")
elif time_of_arrival >= time_of_exam + 60:
    hh = difference // 60
    mm = difference % 60
    if mm < 10:
        print(f"{hh}:0{mm} hours after the start")
    else:
        print(f"{hh}:{mm} hours after the start")


