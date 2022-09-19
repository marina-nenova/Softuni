skumria_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price = skumria_price + (skumria_price * 0.6)
safrid_price = caca_price + (caca_price * 0.8)

midi_total = midi_kg * 7.5
palamud_total = palamud_kg * palamud_price
safrid_total = safrid_kg * safrid_price

total = midi_total + palamud_total + safrid_total
print(f"{total:.2f}")
