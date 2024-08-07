# Program:       rainfall_stats.py
# Programmer:    Lorenzo Openito
# Date:          07/08/2024
# Description:   Conditionals
#####################################


#Lists
names = ["bob", "betty", "liz", "chris"]
heights = [66 ,62, 50, 70]
weights = [150, 100, 140, 110]

#program header
print("BMI Program: \n")
print(f"NAME \tBMI \tCLASSIFICATION")
print()

#loop through lists
for i in range(len(names)):
    #calc bmi
    bmi = (weights[i] * 703)/ (heights[i] * heights[i])
    #provide feedback based on bmi
    if bmi >=25:
        classification = "Overweight"
    elif bmi >=18.5:
        classification = "Healthy"
    elif bmi >= 16:
        classification = "Underweight"
    else:
        classification = "Invalid"
    #detail line
    print(f"{names[i].title()} \t{bmi: .2f} \t{classification}")