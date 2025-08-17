# calculate_discount.py
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage to apply (0-100)
    
    Returns:
    float: Final price after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
    # Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percentage)

# Display the result
if discount_percentage >= 20:
    print(f"After applying a {discount_percentage}% discount, the final price is: ${final_price:.2f}")
else:
    print(f"No discount applied (needs to be 20% or higher). The price remains: ${original_price:.2f}")
# This script calculates the final price after applying a discount
# based on the given conditions.
# The user is prompted to enter the original price and discount percentage.
# The final price is displayed based on the discount criteria.
