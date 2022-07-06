name_of_movie = input()
total_tickets = 0
total_student_tickets = 0
total_standard_tickets = 0
total_kid_tickets = 0
while name_of_movie != "Finish":
    free_seats = int(input())
    counter = 0
    for seat in range(free_seats):
        type_of_seat = input()
        if type_of_seat == "End":
            break
        elif type_of_seat == "student":
            total_student_tickets +=1
        elif type_of_seat == "standard":
            total_standard_tickets += 1
        elif type_of_seat == "kid":
            total_kid_tickets += 1
        counter += 1
        total_tickets +=1
    taken_seats = (counter / free_seats) * 100
    print(f"{name_of_movie} - {taken_seats:.2f}% full.")

    name_of_movie = input()

student_tickets_sold = (total_student_tickets / total_tickets) * 100
standard_tickets_sold = (total_standard_tickets / total_tickets) * 100
kid_tickets_sold = (total_kid_tickets / total_tickets) * 100
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_sold:.2f}% student tickets.")
print(f"{standard_tickets_sold:.2f}% standard tickets.")
print(f"{kid_tickets_sold:.2f}% kids tickets.")