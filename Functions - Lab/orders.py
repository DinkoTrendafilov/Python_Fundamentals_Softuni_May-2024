def calculate_product_total_price(product_name, quantity_of_product):
    total_price = 0
    if product_name == "coffee":
        price = 1.50
        total_price = price * quantity_of_product

    elif product_name == "water":
        price = 1.00
        total_price = price * quantity_of_product

    elif product_name == "coke":
        price = 1.40
        total_price = price * quantity_of_product

    elif product_name == "snacks":
        price = 2.00
        total_price = price * quantity_of_product

    formated_total_price = f"{total_price:.2f}"
    return formated_total_price


product = input()
quantity = int(input())

result_func = calculate_product_total_price(product, quantity)
print(result_func)
