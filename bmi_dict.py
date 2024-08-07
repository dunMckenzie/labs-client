# Program:       bmi_dict.py
# Programmer:    Lorenzo Openito
# Date:          08/08/2024
# Description:   Conditionals with lists and dictionaries
#####################################

# Define and initialize dictionaries for patients
patient_0 = {"name": "bob", "height": 66, "weight": 150}
patient_1 = {"name": "betty", "height": 62, "weight": 100}
patient_2 = {"name": "liz", "height": 50, "weight": 140}
patient_3 = {"name": "chris", "height": 70, "weight": 110}

# Store the dictionaries in a list
patients = [patient_0, patient_1, patient_2, patient_3]

# Program header
print("BMI Program: \n")
print(f"NAME \tBMI \tCLASSIFICATION")
print()

# Loop through the list and calculate BMI
for patient in patients:
    name = patient["name"]
    height = patient["height"]
    weight = patient["weight"]
    
    # Calculate BMI
    bmi = (weight * 703) / (height * height)
    
    # Determine classification
    if bmi >= 25:
        classification = "Overweight"
    elif bmi >= 18.5:
        classification = "Healthy"
    elif bmi >= 16:
        classification = "Underweight"
    else:
        classification = "Invalid"

    # Print detail line
    print(f"{name.title()} \t{bmi: .2f} \t{classification}")

# Thank you message
print("\nThanks for using this program!")
