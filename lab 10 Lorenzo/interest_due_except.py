import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

repeat = True

while repeat:
    clear_terminal()
    print("Program - Calculate Interest on Loan:")
    
    try:
        amount = float(input("How many dollars do you wish to borrow? "))
    except ValueError:
        print("Input Error >>> Please enter numbers only")
        continue
    
    try:
        interest_rate = float(input("What is the interest rate? "))
    except ValueError:
        print("Input Error >>> Please enter numbers only")
        continue
    
    try:
        years = int(input("How many years would you take the loan? "))
    except ValueError:
        print("Input Error >>> Please enter numbers only")
        continue
    
    total_interest = amount * (interest_rate / 100) * years
    
    output = f"\nIf you borrow ${amount:.2f} at an interest rate of {interest_rate}%"
    output += f"\nfor {years} years, you will pay ${total_interest:.2f} in interest."
    print(output)
    
    again = input("\nWould you like to run another calculation? (y/n) ").lower()
    if again == 'n':
        repeat = False

print("\nThanks for using this program. Goodbye!")
