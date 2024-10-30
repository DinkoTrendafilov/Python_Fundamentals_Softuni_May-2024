import re

n = int(input())

for _ in range(n):
    barcode = input().strip()
    pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

    if re.fullmatch(pattern, barcode):
        digits = re.findall(r"\d", barcode)
        if digits:
            product_group = ''.join(digits)
        else:
            product_group = '00'
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")