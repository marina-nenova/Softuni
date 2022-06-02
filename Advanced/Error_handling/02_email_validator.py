class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def domain_is_invalid(valid_domains, domain):
    is_invalid = True
    for valid_domain in valid_domains:
        if domain.endswith(valid_domain):
            is_invalid = False
            break
    return is_invalid


email = input()
valid_domains = [".com", ".bg", ".net", ".org"]

while not email == "End":

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain = email.split("@")

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    
    if domain_is_invalid(valid_domains, domain):
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

    print("Email is valid")

    email = input()
