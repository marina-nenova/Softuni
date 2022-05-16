number_of_days = int(input())
doctors = 7
treated = 0
untreated = 0

for day in range(1, number_of_days + 1):
    number_of_patients = int(input())
    if day % 3 == 0 and untreated > treated:
        doctors += 1
    if number_of_patients <= doctors:
        treated += number_of_patients
    else:
        treated += doctors
        untreated += number_of_patients - doctors
print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")