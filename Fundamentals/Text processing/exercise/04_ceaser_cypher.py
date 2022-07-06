text = input()

encrypted_text = ""

for character in text:
    char_code = ord(character)
    encrypted_char_code = char_code + 3
    encrypted_text += chr(encrypted_char_code)

print(encrypted_text)