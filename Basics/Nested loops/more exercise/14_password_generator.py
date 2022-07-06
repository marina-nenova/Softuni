n = int(input())
l = int(input())

for symbol1 in range(1, n + 1):
    for symbol2 in range(1, n + 1):
        for symbol3 in range(ord("a"), ord("a") + l):
            for symbol4 in range(ord("a"), ord("a") + l):
                for symbol5 in range(1, n + 1):
                    if symbol5 > symbol1 and symbol5 > symbol2:
                        print(f"{symbol1}{symbol2}{chr(symbol3)}{chr(symbol4)}{symbol5}", end = " ")