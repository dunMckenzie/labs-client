# Program: drop_grade_refactored.py
# Programmer: Lorenzo Openito
# Date: 09/08/2024
# Description: Calculate current and projected sales for the week

def show_grades(grades):
    print("Grades:")
    for grade in grades:
        print(grade)

def display_grade_stats(grades):
    total = sum(grades)
    average = total / len(grades)
    print(f"Number of grades: {len(grades)}")
    print(f"Average: {average:.2f}")

def display_lowest_grade(grades):
    lowest_grade = min(grades)
    print(f"Lowest grade: {lowest_grade}")

def drop_lowest_grade(grades):
    lowest_grade = min(grades)
    grades.remove(lowest_grade)
    print("\nLOWEST GRADE DROPPED.")

def main():
    print("DROP LOWEST GRADE PROGRAM\n")
    grades = [100, 80, 70, 60, 90]
    
    show_grades(grades)
    display_grade_stats(grades)
    display_lowest_grade(grades)
    
    drop_lowest_grade(grades)
    
    print("\nGrades:")
    show_grades(grades)
    display_grade_stats(grades)
    display_lowest_grade(grades)
    print()

if __name__ == "__main__":
    main()
