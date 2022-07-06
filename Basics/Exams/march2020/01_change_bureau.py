number_of_bitcoins = int(input())
number_of_uans = float(input())
comission = float(input())

bitcoin_in_lv = number_of_bitcoins * 1168
uians_in_usd = number_of_uans * 0.15
uans_in_lv = uians_in_usd * 1.76
total_lv = uans_in_lv + bitcoin_in_lv
eur = total_lv / 1.95
exchange_comission = eur * (comission / 100)
total_eur = eur - exchange_comission
print(f"{total_eur:.2f}")