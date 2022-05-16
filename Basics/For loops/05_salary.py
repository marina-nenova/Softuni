number_of_tabs = int(input())
salary = int(input())

for tab in range(number_of_tabs):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50
    else:
        fine = 0

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)
