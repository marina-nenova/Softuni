num_of_pens = int(input())
num_of_markers = int(input())
detergent = int(input())
discount = int(input())

pens_sum = num_of_pens * 5.8
markers_sum = num_of_markers * 7.2
detergent_sum = detergent * 1.2
discount_in_percent = discount / 100

total = pens_sum + markers_sum + detergent_sum
final_sum = total - total * discount_in_percent
print(final_sum)