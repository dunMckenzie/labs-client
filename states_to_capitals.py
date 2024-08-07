# Program:       states_to_capital.py
# Programmer:    Lorenzo Openito
# Date:          08/08/2024
# Description:   Dictionaries
####################################

states_to_capital = {'texas': 'austin',
                     'new york': 'albany',
                     'louisiana': 'baton rouge',
                     'georgia': 'atlanta'
                     }

print("State Capitals Listing\n")

for key, value in states_to_capital.items():
    print(f"The capital of {key.title()} is {value.title()}.")

print("\nDelete New York. ")
del states_to_capital['new york']
print(f"\n Number of states in this report: {len(states_to_capital)}")

print("\nAdding Michigan and relisting")
states_to_capital['michigan'] = 'lansing'

print()
for key, value in states_to_capital.items():
    print(f"The capital of {key.title()} is {value.title()}")

print(f"\n Number of states in this report: {len(states_to_capital)}")
print()