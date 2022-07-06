import string

secret_word = ""
password = ""
c_counter = 0
o_counter = 0
n_counter = 0
letter = input()
while letter != "End":
    if letter in string.ascii_lowercase or letter in string.ascii_uppercase:
        if letter == "c" and c_counter == 0:
            c_counter += 1
        elif letter == "c" and c_counter == 1:
            secret_word += letter
        elif letter == "o" and o_counter == 0:
            o_counter += 1
        elif letter == "o" and o_counter == 1:
            secret_word += letter
        elif letter == "n" and n_counter == 0:
            n_counter += 1
        elif letter == "n" and n_counter == 1:
            secret_word += letter
        else:
            secret_word += letter
        if c_counter == 1 and o_counter == 1 and n_counter == 1:
            secret_word += " "
            c_counter = 0
            o_counter = 0
            n_counter = 0
            password = secret_word

    letter = input()
print(password)