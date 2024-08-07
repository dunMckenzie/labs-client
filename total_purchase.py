# Program: total_purchase.py
# Programmer: Lorenzo Openito
# Date: 07/08/2024
# Description: Lab 2 - Calculate the total purchase price of four items including sales tax

# declare constant for sales tax rate and set to 6%
SALES_TAX_RATE = 0.06

# initialize numeric variables to hold price of four sales items
item1_price = 175.00
item2_price = 125.00
item3_price = 300.00
item4_price = 100.00

# calc subtotal
subtotal = item1_price + item2_price + item3_price + item4_price

# calc sales tax
sales_tax = subtotal * SALES_TAX_RATE

# calc grand total
grand_total = subtotal + sales_tax

# print name of program
print("Total Purchase Calculation")
print("-" * 30)

# display items and their cost in f string in two columns
print(f"Item 1: \t\t${item1_price:>7.2f}")
print(f"Item 2: \t\t${item2_price:>7.2f}")
print(f"Item 3: \t\t${item3_price:>7.2f}")
print(f"Item 4: \t\t${item4_price:>7.2f}")

# display single dash line as a separator line
print("-" * 30)

# display subtotal, sales tax, and grand total
print(f"Subtotal: \t\t${subtotal:>7.2f}")
print(f"Sales Tax (6%): \t${sales_tax:>7.2f}")
print(f"Grand Total: \t\t${grand_total:>7.2f}")

# display double dash line as a separator line
print("=" * 30)

# print statement used to add blank line at the end
print()
