number_of_clients = int(input())
product_price = 0
total = 0
for client in range(number_of_clients):
    command = input()
    products_counter = 0
    client_total = 0
    while command != "Finish":
        type_of_product = command
        products_counter += 1
        if type_of_product == "basket":
            product_price = 1.5
        elif type_of_product == "wreath":
            product_price = 3.8
        elif type_of_product == "chocolate bunny":
            product_price = 7
        client_total += product_price
        command = input()
    if products_counter % 2 == 0:
        client_total -= client_total * 0.2
    total += client_total

    print(f"You purchased {products_counter} items for {client_total:.2f} leva.")
average_bill = total / number_of_clients
print(f"Average bill per client is: {average_bill:.2f} leva.")