print("Program - Calculate Interest on loan: ")

repeat = True

while repeat:
    amount = input("\How many dollars do you wish to borrow? ")
    amount = float(amount)
    interest_rate = float(input("What is the interest rate? "))
    years = int(int(input("How many years would you take the loan? ")))

    total_interest = amount * (interest_rate/100) * years

    output = f"\nIf you borrow {amount} at an interest rate of {interest_rate}"
    output += f"\nfor {years} years, you will pay {total_interest} in interest. "

    print(output)

    again = input("\nWouldyou like to run another calculation? (y/n)")

    if again == 'n':
        repeat = False

print("\nThanks for using this  program. Goodbye!")


