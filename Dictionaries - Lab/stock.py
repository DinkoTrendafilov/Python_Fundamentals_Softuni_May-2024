items = input().split()
bakery = {}

for i in range(0, len(items), 2):
    product_name = items[i]
    quantity = items[i + 1]
    if product_name not in bakery:
        bakery[product_name] = int(quantity)
    else:
        bakery[product_name] += int(quantity)

searched_products = input().split()

for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
