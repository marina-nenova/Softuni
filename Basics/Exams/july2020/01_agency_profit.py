name_of_company = input()
adult_tickets = int(input())
kids_tickets = int(input())
adult_tickets_prise = float(input())
service_fee = float(input())

adult_tickets_total = (adult_tickets_prise + service_fee) * adult_tickets
kids_tickets_price = (adult_tickets_prise * 0.3) + service_fee
kids_tickets_total = kids_tickets * kids_tickets_price
total_tickets_sold = adult_tickets_total + kids_tickets_total
profit = total_tickets_sold * 0.2

print(f"The profit of your agency from {name_of_company} tickets is {profit:.2f} lv.")

