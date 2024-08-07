#Program:        interest.py
#programmer:     Lorenzo Openito
#Date:           07/08/2024
#Description:    lab 2 - numeric variables
# ###############################################


#declare variables
years =15
rate  = 6 
loan = 5000

interest = loan * (rate / 100) * years

#show output

print(f"Loan amount: \t${loan:,.2f}")
print(f"Interest rate: \t{rate}%")
print(f"No. of years: \t{years}")
print(f"Interest paid: \t${interest:,.2f}")