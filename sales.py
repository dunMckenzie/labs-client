# Program:       sales.py
# Programmer:    Lorenzo Openito
# Date:          07/08/2024
# Description:   Calculate current and projected sales for the week
###################################################

# initialize list of days of the week starting with Monday abbreviated lowercase
days_of_week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

# initialize list of daily sales as provided corresponding to days of week
daily_sales = [1000, 2000, 3000, 4000, 5000, 6000, 7000]

# initialize list for projected daily sales and populate with 7 zeros
projected_sales = [0, 0, 0, 0, 0, 0, 0]

# declare constant to hold projected increase and assign 1.05 to it
PROJECTED_INCREASE = 1.05

# calculate projected daily sales for each day of the week
projected_sales[0] = daily_sales[0] * PROJECTED_INCREASE
projected_sales[1] = daily_sales[1] * PROJECTED_INCREASE
projected_sales[2] = daily_sales[2] * PROJECTED_INCREASE
projected_sales[3] = daily_sales[3] * PROJECTED_INCREASE
projected_sales[4] = daily_sales[4] * PROJECTED_INCREASE
projected_sales[5] = daily_sales[5] * PROJECTED_INCREASE
projected_sales[6] = daily_sales[6] * PROJECTED_INCREASE

# print report header
print("ACME Stores Incorperated Sales Report: \n")

# print current sales for each day of the week
print("Current Sales:\n")
print(f"{days_of_week[0].capitalize()}\t${daily_sales[0]:,.2f}")
print(f"{days_of_week[1].capitalize()}\t${daily_sales[1]:,.2f}")
print(f"{days_of_week[2].capitalize()}\t${daily_sales[2]:,.2f}")
print(f"{days_of_week[3].capitalize()}\t${daily_sales[3]:,.2f}")
print(f"{days_of_week[4].capitalize()}\t${daily_sales[4]:,.2f}")
print(f"{days_of_week[5].capitalize()}\t${daily_sales[5]:,.2f}")
print(f"{days_of_week[6].capitalize()}\t${daily_sales[6]:,.2f}")

# print projected 5% increase in sales for each day of the week
print("\nProjected Sales (5% Increase):\n")
print(f"{days_of_week[0].capitalize()}\t${projected_sales[0]:,.2f}")
print(f"{days_of_week[1].capitalize()}\t${projected_sales[1]:,.2f}")
print(f"{days_of_week[2].capitalize()}\t${projected_sales[2]:,.2f}")
print(f"{days_of_week[3].capitalize()}\t${projected_sales[3]:,.2f}")
print(f"{days_of_week[4].capitalize()}\t${projected_sales[4]:,.2f}")
print(f"{days_of_week[5].capitalize()}\t${projected_sales[5]:,.2f}")
print(f"{days_of_week[6].capitalize()}\t${projected_sales[6]:,.2f}")
