# Program:       southern_states_loop.py
# Programmer:    Lorenzo Openito
# Date:          07/08/2024
# Description:   Python lists with loops
###################################################

# Initialize a list with names of the southern states all lowercase
southern_states = [
    'virginia', 'tennessee', 'arkansas', 'louisiana', 
    'north carolina', 'south carolina', 'mississippi',
    'alabama', 'georgia', 'florida', 'texas'
]

# Print name of report
print("Report - Southern United States\n")

# Show unsorted list using for in loop - show title case
print("UNSORTED:\n")
for state in southern_states:
    print(state.title())

# Use negative index to access last element in list and show it in title case
print(f"\nLast state on this unsorted list: {southern_states[-1].title()}\n")

# Sort the list using the sort method
southern_states.sort()

# Show sorted list using while loop
print("SORTED:\n")
index = 0
while index < len(southern_states):
    print(southern_states[index].title())
    index += 1

# Use negative index to access last element in list
print(f"\nLast state on this ordered list: {southern_states[-1].title()}\n")

print(f"Number of Southern States: {len(southern_states)}")
# Show length of list
print(f"\nSource: simple.wikipedia.org/wiki/Southern_United_States")
