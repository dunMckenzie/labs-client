# Program:       grades_write.py
# Programmer:    Lorenzo Openito
# Date:          8/08/2024
# Description:   write contents to a file
# ###################################################




from pathlib import Path

# Create a Path object representing the file path
file_path = Path("/home/lorenzo/labs/grades.txt")

# Define the contents of the file
grades_data = """\
111 Olivera 90
222 Benavides 80
333 Gonzalez 70
444 Casas 60
555 Ramirez 50
"""

# Write the contents to the file
file_path.write_text(grades_data)
