# Program: employee_client.py
# Programmer: Lorenzo Openito
# Date: 09/08/2024
# Description: Client program to interact with Employee class and manage raises

from employee_class import Employee

def main():
    employee = Employee("Eric", "Matthes", 65000)
    
    choice = input("Give Eric a default raise of 5K or custom raise of 10K?\n- (d for default or c for custom): ").lower()
    
    if choice == 'd':
        employee.give_raise()
        print(f"\nFirst Name: {employee.first_name}")
        print(f"Last Name: {employee.last_name}")
        print(f"Current Salary: ${employee.annual_salary - 5000:.2f}")
        print(f"Salary after default raise of 5K: ${employee.annual_salary:.2f}")
    elif choice == 'c':
        employee.give_raise(10000)
        print(f"\nFirst Name: {employee.first_name}")
        print(f"Last Name: {employee.last_name}")
        print(f"Current Salary: ${employee.annual_salary - 10000:.2f}")
        print(f"Salary after custom raise of 10K: ${employee.annual_salary:.2f}")

if __name__ == "__main__":
    main()
