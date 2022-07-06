name_of_movie = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while name_of_movie != "Finish":
    free_seats = int(input())
    tickets_sold = 0
    for seat in range(free_seats):
        type_of_ticket = input()
        if type_of_ticket == "End":
            break
        elif type_of_ticket == "student":
            student_tickets += 1
        elif type_of_ticket == "standard":
            standard_tickets += 1
        elif type_of_ticket == "kid":
            kid_tickets += 1
        tickets_sold += 1
    percentage_full = (tickets_sold / free_seats) * 100
    print(f"{name_of_movie} - {percentage_full:.2f}% full.")
    name_of_movie = input()

total_tickets = student_tickets + standard_tickets + kid_tickets
student_tickets_percentage = (student_tickets / total_tickets) * 100
standard_tickets_percentage = (standard_tickets / total_tickets) * 100
kid_tickets_percentage = (kid_tickets / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_percentage:.2f}% student tickets.")
print(f"{standard_tickets_percentage:.2f}% standard tickets.")
print(f"{kid_tickets_percentage:.2f}% kids tickets.")


