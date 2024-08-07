##Program:       determine_season.py
# Programmer:    Lorenzo Openito
# Date:          8/08/2024
# Description:   This program receives a Fahrenheit temperature and determines the probable season.
###################################################


def determine_season(temp):
    """Determine the season based on the given temperature."""
    if temp > 130 or temp < -20:
        season = "invalid"
    elif temp >= 90:
        season = "summer"
    elif temp >= 70 and temp < 90:
        season = "spring"
    elif temp >= 50 and temp < 70:
        season = "fall"
    elif temp < 50:
        season = "winter"
    else:
        season = ""
    return season

# Print the name of the program
print("Program - Determine Season Based on Temperature")

# Set the repeat flag to True
repeat = True

while repeat:
    # Prompt for temperature and convert to float
    temp = float(input("\nEnter the temperature in Fahrenheit: "))

    # Find the season by calling the function, passing temp, and assigning the return to a variable
    season = determine_season(temp)

    # Print output stating the temp and season using title case
    print(f"Based on the temperature of {temp}°F, it is most likely {season.title()}.")

    # Prompt for again and set the flag accordingly
    again = input("\nWould you like to enter another temperature? (y/n): ")
    if again.lower() == 'n':
        repeat = False

# Print thanks and goodbye on exit
print("\nThanks for using this program. Goodbye.\n")
