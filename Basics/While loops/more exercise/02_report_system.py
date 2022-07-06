expected_total = int(input())

money_collected = 0
counter = 0
cs = 0
cs_counter = 0
cc = 0
cc_counter = 0
while money_collected < expected_total:
    counter += 1
    item_price = input()
    if item_price == "End":
        print("Failed to collect required money for charity.")
        break
    if counter % 2 == 1:
        if int(item_price) > 100:
            print("Error in transaction!")
        else:
            money_collected += int(item_price)
            cs += int(item_price)
            cs_counter += 1
            print("Product sold!")
    elif counter %2 == 0:
        if int(item_price) < 10:
            print("Error in transaction!")
        else:
            money_collected += int(item_price)
            cc += int(item_price)
            cc_counter += 1
            print("Product sold!")

if money_collected >= expected_total:
    average_cs = cs / cs_counter
    average_cc = cc / cc_counter
    print(f"Average CS: {average_cs:.2f}")
    print(f"Average CC: {average_cc:.2f}")