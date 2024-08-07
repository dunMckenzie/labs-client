# Program:       drop_grade.py
# Programmer:    Lorenzo Openito
# Date:          07/08/2024
# Description:   Calculate current and projected sales for the week
###################################################

grades = [100, 80, 70, 60,90]

print("DROP LOWEST GRADE PROGRAM \n")

for grade in grades:
    print(grade)

total = sum(grades)
average = total/len(grades)
 
print(f"Number of grades: {len(grades)}")
print(f"Average: {average: .2f}")
lowest_grade= min(grades)
print(f"lowest grade: {lowest_grade}")
grade_lowest_index = grades.index(lowest_grade)
del grades[grade_lowest_index]

print("\nLOWEST GRADE DROPPED. ")

print("\nGrade: ")

for grade in grades:
    print(grade)

total = sum(grades)
average = total/len(grades)
 
print(f"Number of grades: {len(grades)}")
print(f"Average: {average: .2f}")
lowest_grade= min(grades)
print(f"lowest grade: {lowest_grade}")
print()
