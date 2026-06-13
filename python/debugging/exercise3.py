def calculate_discount(price, discount):
    final_price = price - discount
    return final_price

amount = calculate_discount(100, 20)
print("The final price after discount is:", amount) 