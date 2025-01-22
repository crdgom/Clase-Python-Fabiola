# Main application that uses the modules

from employee import create_employee, list_employees, update_employee, delete_employee
from utils import get_int_input, get_str_input

def show_menu():
    """Displays the main menu."""
    print("\n--- Main Menu ---")
    print("1. Create Employee")
    print("2. List Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

def main():
    """Main entry point of the application."""
    while True:
        show_menu()
        option = get_int_input("Choose an option: ")

        if option == 1:
            print("\n--- Create Employee ---")
            name = get_str_input("Name: ")
            age = get_int_input("Age: ")
            position = get_str_input("Position: ")
            print(create_employee(name, age, position))

        elif option == 2:
            print("\n--- List Employees ---")
            print(list_employees())

        elif option == 3:
            print("\n--- Update Employee ---")
            employee_id = get_int_input("Enter the ID of the employee to update: ")
            print("Leave fields blank to keep them unchanged.")
            name = get_str_input("New name (or press Enter to skip): ")
            age_input = input("New age (or press Enter to skip): ")
            age = int(age_input) if age_input else None
            position = get_str_input("New position (or press Enter to skip): ")
            print(update_employee(employee_id, name=name if name else None, age=age, position=position if position else None))

        elif option == 4:
            print("\n--- Delete Employee ---")
            employee_id = get_int_input("Enter the ID of the employee to delete: ")
            print(delete_employee(employee_id))

        elif option == 5:
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()