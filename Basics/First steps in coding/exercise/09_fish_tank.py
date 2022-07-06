length = int(input())
width = int(input())
hight = int(input())
taken_volume = float(input())

taken_volume_in_percent = taken_volume / 100
aquarium_volume = length * width * hight
volume_in_litres = aquarium_volume * 0.001
needed_litres = volume_in_litres * (1 - taken_volume_in_percent)
print(needed_litres)