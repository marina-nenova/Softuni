import re


def product_group(valid_bc):
    product_group = ""
    for ch in valid_bc:
        if ch.isdigit():
            product_group += str(ch)
    if product_group == "":
        return "00"
    else:
        return product_group


n = int(input())
pattern = r"@#+(?P<valid>[A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

for _ in range(n):
    barcode = input()
    matches = re.search(pattern, barcode)
    if not matches:
        print("Invalid barcode")
    else:
        valid_barcode = matches.group("valid")
        print(f"Product group: {product_group(valid_barcode)}")
