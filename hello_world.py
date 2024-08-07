# hello_world.py
# Author: Lorenzo Openito
# Date: 2024-08-07
# Description: This program prints "Hello, World!" five times cascading to the right,
# gives credit to the person who first wrote the program, and then prints
# "Hello, World!" five times cascading to the left.

# Declare variables and initialize
program = "hello, world!"
computer_scientist = "brian kernighan"
year_created = 1978

# Print blank line
print()

# Print the program variable five times cascading to right – use title case
print(f"\t{program.title()}")
print(f"\t\t{program.title()}")
print(f"\t\t\t{program.title()}")
print(f"\t\t\t\t{program.title()}")
print(f"\t\t\t\t\t{program.title()}")
# Print blank line
print()

# Use formatted string to print sentence giving credit to that person
print(f'\"{program.title()}\" was created by {computer_scientist.title()} in {year_created}.\n')

# Print blank line
print()

# Print the program variable five times cascading to left – use title case

print(f"\t\t\t\t\t{program.title()}")
print(f"\t\t\t\t{program.title()}")
print(f"\t\t\t{program.title()}")
print(f"\t\t{program.title()}")
print(f"\t{program.title()}")
