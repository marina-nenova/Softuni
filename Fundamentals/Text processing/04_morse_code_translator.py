morse = {'.-': 'A', '-...': 'B', '-.-.': 'C',
       '-..': 'D', '.': 'E', '..-.': 'F',
       '--.': 'G', '....': 'H', '..': 'I',
       '.---': 'J', '-.-': 'K', '.-..': 'L',
       '--': 'M', '-.': 'N', '---': 'O',
       '.--.': 'P', '--.-': 'Q', '.-.': 'R',
       '...': 'S', '-': 'T', '..-': 'U',
       '...-': 'V', '.--': 'W', '-..-': 'X',
       '-.--': 'Y', '--..': 'Z', '-----': '0',
       '.----': '1', '..---': '2', '...--': '3',
       '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'}

morse_code_words = input().split("|")
message = ""

for word in morse_code_words:
    letters = word.split()
    for letter_code in letters:
        message += morse[letter_code]
    message += " "

print(message.rstrip())