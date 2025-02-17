# Program:       rectangle_season.py
# Programmer:    Lorenzo Openito
# Date:          8/08/2024
# Description:   Python modules
###################################################


import rectangle_mod

print("Program - Find Area and Perimeter of Rectangle: ")

repeat = True

while repeat:
    width = input("\nEnter the rectangle's width (inches): ")
    width = float(width)
    length = float(input("Enter the rectangle's length (inches): "))

    area = rectangle_mod.find_area(width, length)
    perimeter = rectangle_mod.find_perimeter(width, length)

    print(f"The area is {area: .0f}")
    print(f"The perimeter is {perimeter: .0f}")

    again = input("\nWould you like to do another calculation? (y/n)")
    if again == 'n':
        repeat = False

print("\nThanks for using this program. Goodbye. \n")




