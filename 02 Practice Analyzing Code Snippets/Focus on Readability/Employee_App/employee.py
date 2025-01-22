# Module to handle employee-related operations

employees = []  # List to store employee information

def create_employee(name, age, position):
    """Creates a new employee and adds it to the list."""
    employee_id = len(employees) + 1
    employees.append({"id": employee_id, "name": name, "age": age, "position": position})
    return f"Employee {name} created with ID {employee_id}."

def list_employees():
    """Returns a list of registered employees."""
    if not employees:
        return "No employees registered."
    return "\n".join(
        [f"ID: {emp['id']}, Name: {emp['name']}, Age: {emp['age']}, Position: {emp['position']}" for emp in employees]
    )

def update_employee(employee_id, name=None, age=None, position=None):
    """Updates the information of an existing employee."""
    for emp in employees:
        if emp["id"] == employee_id:
            if name:
                emp["name"] = name
            if age:
                emp["age"] = age
            if position:
                emp["position"] = position
            return f"Employee with ID {employee_id} updated."
    return f"Employee with ID {employee_id} not found."

def delete_employee(employee_id):
    """Removes an employee from the list."""
    global employees
    for emp in employees:
        if emp["id"] == employee_id:
            employees = [e for e in employees if e["id"] != employee_id]
            return f"Employee with ID {employee_id} deleted."
    return f"Employee with ID {employee_id} not found."
