# Program:       grades_read.py
# Programmer:    Lorenzo Openito
# Date:          8/08/2024
# Description:   read contents from a file
# ###################################################



from pathlib import Path

# Create a Path object representing the file path
file_path = Path("/home/lorenzo/labs/grades.txt")

# Initialize counters
grade_count = 0
grade_sum = 0

try:
    # Read the contents of the file
    grades_data = file_path.read_text()
    
    # Print header
    print(f"{'ID':<10}{'Name':<15}{'Grade':>10}")
    print("-" * 35)
    
    # Split the contents into lines and process each line
    for line in grades_data.strip().split('\n'):
        student_id, last_name, grade = line.split()
        grade = int(grade)  # Convert grade to int
        
        # Print formatted student data
        print(f"{student_id:<10}{last_name:<15}{grade:>10}")
        
        # Update counters
        grade_count += 1
        grade_sum += grade
    
    # Print footer with number of grades and average grade
    print("-" * 35)
    print(f"Number of Grades: {grade_count}")
    print(f"Average: {grade_sum / grade_count:.2f}")

except FileNotFoundError:
    print("Sorry, grades.txt not found. Please contact system admin.")
except TypeError:
    print("Sorry, unsupported operation. Please see system admin.")
except Exception as e:
    print(f"An error has occurred. Please see system admin. Error: {e}")
