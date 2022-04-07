def password_validator(input_password):
    password_is_invalid = False
    if len(input_password) > 10 or len(password) < 6:
        print("Password must be between 6 and 10 characters")
        password_is_invalid = True
    if not input_password.isalnum():
        print("Password must consist only of letters and digits")
        password_is_invalid = True
    if sum(map(str.isdigit, input_password)) < 2:
        print("Password must have at least 2 digits")
        password_is_invalid = True
    if not password_is_invalid:
        print("Password is valid")


password = input()
password_validator(password)

