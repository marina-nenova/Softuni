import re

num = int(input())
key_pattern = r"[star]"
decrypt_pattern = r"[^@!:>-]*@(?P<planet>[A-Za-z]+)[^@!:>-]*:(?P<population>\d+)[^@!:>-]*!(?P<type>[A|D])![^@!:>-]*->(?P<soldiers>\d+)"
attacked_planets = []
destroyed_planets = []

for i in range(num):
    message = input()
    key = len(re.findall(key_pattern, message, re.IGNORECASE))
    decrypted_message = ""
    for char in message:
        decrypted_message += chr(ord(char) - key)

    match = re.search(decrypt_pattern, decrypted_message)
    if match is not None:
        if match.group("type") == "A":
            attacked_planets.append(match.group("planet"))
        elif match.group("type") == "D":
            destroyed_planets.append(match.group("planet"))

print(f"Attacked planets: {len(attacked_planets)}")
for a_planet in sorted(attacked_planets):
    print(f"-> {a_planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for d_planet in sorted(destroyed_planets):
    print(f"-> {d_planet}")
