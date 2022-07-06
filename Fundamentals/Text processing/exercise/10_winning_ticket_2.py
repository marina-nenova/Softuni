import re

tickets = [ticket.strip() for ticket in input().split(",")]
symbols_pattern = r"(\@{6,10}|\${6,10}|\^{6,10}|\#{6,10})"

for ticket in tickets:
    match_length = 0
    if len(ticket) != 20:
        print("invalid ticket")

    else:
        left_half = ticket[:10]
        right_half = ticket[10:]
        left_side_match = "".join(re.findall(symbols_pattern, left_half))
        right_side_match = "".join(re.findall(symbols_pattern, right_half))

        if (left_side_match and right_side_match) and (left_side_match[0] == right_side_match[0]):
            winning_symbol = left_side_match[0]
            match_length = min(len(left_side_match), len(right_side_match))
            if match_length < 10:
                print(f'ticket "{ticket}" - {match_length}{winning_symbol}')
            else:
                print(f'ticket "{ticket}" - {match_length}{winning_symbol} Jackpot!')
        else:
            print(f'ticket "{ticket}" - no match')
