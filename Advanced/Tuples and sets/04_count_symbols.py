text = input()

symbols_count = {}

for ch in text:
    if ch not in symbols_count:
        symbols_count[ch] = 0
    symbols_count[ch] += 1

for data in sorted(symbols_count.items()):
    print(f"{data[0]}: {data[1]} time/s")
