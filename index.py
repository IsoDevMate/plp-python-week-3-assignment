def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage (0-100)

    Returns:
        float: The final price after discount (if applicable)
    """
    # Only apply discount if it's 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

def main():
    # Prompt user for inputs
    try:
        # take original price
        original_price = float(input("Enter the original price of the item: $"))
        if original_price < 0:
            print("Error: Price cannot be negative.")
            return

        # take discount percentage
        discount_percent = float(input("Enter the discount percentage (0-100): "))
        if discount_percent < 0 or discount_percent > 100:
            print("Error: Discount percentage must be between 0 and 100.")
            return

        # Calculate final price using our function
        final_price = calculate_discount(original_price, discount_percent)

        # Display results
        if final_price < original_price:
            discount_applied = original_price - final_price
            print(f"\nOriginal price: ${original_price:.2f}")
            print(f"Discount applied: ${discount_applied:.2f} ({discount_percent:.1f}%)")
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print(f"\nOriginal price: ${original_price:.2f}")
            print(f"No discount applied (discount must be 20% or higher)")
            print(f"Final price: ${final_price:.2f}")

    except ValueError:
        print("Error: Please enter valid numerical values for price and discount percentage.")

if __name__ == "__main__":
    main()
