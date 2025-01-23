class Employees:
    """Representa a un empleado con información básica y habilidades."""
    
    def __init__(self, name, employee_id, role, skills=None):
        self.name = name
        self.employee_id = employee_id
        self.role = role
        self.skills = skills if skills else []

    def add_skill(self, skill):
        """Agrega una nueva habilidad al conjunto de habilidades del empleado."""
        if skill not in self.skills:
            self.skills.append(skill)

    def display_info(self):
        """Muestra la información básica del empleado."""
        print(f"ID: {self.employee_id}, Nombre: {self.name}, Rol: {self.role}")
        print("Habilidades:", ", ".join(self.skills) if self.skills else "Sin habilidades")

# Creación de empleados
employees = [
    Employee("Carlos", 101, "Desarrollador", ["Python", "Django"]),
    Employee("Ana", 102, "Diseñadora"),
    Employee("Luis", 103, "Gestor de proyectos")
]

# Agregar habilidades a empleados
employees[0].add_skill("")
employees[0].add_skill("React")
employees[1].add_skill("Photoshop")
employees[2].add_skill("Gestión ágil")

# Mostrar información
for employee in employees:
    employee.display_info()