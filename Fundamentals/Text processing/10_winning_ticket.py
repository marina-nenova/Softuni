def is_winning(ticket):
    if not len(ticket) == 20:
        return "invalid ticket"
    left_side = ticket[:10]
    right_side = ticket[10:]
    winning_symbols = ["@", "#", "$", "^"]
    for winning_char in winning_symbols:
        for repetition in range(10, 5, -1):
            char_repetition = winning_char * repetition
            if char_repetition in left_side and char_repetition in right_side:
                if repetition == 10:
                    return f'ticket "{ticket}" - {repetition}{winning_char} Jackpot!'
                elif 6 <= repetition <= 9:
                    return f'ticket "{ticket}" - {repetition}{winning_char}'
    return f'ticket "{ticket}" - no match'


tickets = [s.strip() for s in input().split(", ")]
results = []
for ticket in tickets:
    results.append(is_winning(ticket))

for result in results:
    print(result)
