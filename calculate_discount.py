def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

#  prompt the user to enter the original price of an item and the discount percentage. 
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)
    
    if discount_percent >= 20:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount was applied. The original price is: {original_price:.2f}")
    
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")  