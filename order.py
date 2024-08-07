# Program:       order.py
# Programmer:    Lorenzo Openito
# Date:          08/08/2024
# Description:   Sum the order at a hamburger restaurant

# Create parallel lists for menu items and their prices
menu_items = ["hamburger", "soda", "fries", "chicken nuggets", "coffee", "cheeseburger"]
menu_prices = [3.00, 1.25, 2.00, 2.90, 0.90, 3.40]

# Create a customer order list
customer_order = ["hamburger", "fries", "soda", "pizza"]

# Initialize the total price accumulator variable
total_price = 0.0

# Print the program header
print("Order Detail:\n")

# Loop through the customer order list
for item in customer_order:
    if item in menu_items:
        # Get the index of the menu item
        index = menu_items.index(item)
        # Get the price of the menu item
        price = menu_prices[index]
        # Print the item and its price
        print(f"{item.title()}: ${price:.2f}")
        # Increment the total price
        total_price += price
    else:
        # Print feedback if the item is not on the menu
        print(f"Sorry, we don't have {item}.")

# Print the total price of the order
print("\nYour order is ready!.")
print(f"Total price: ${total_price:.2f}")
