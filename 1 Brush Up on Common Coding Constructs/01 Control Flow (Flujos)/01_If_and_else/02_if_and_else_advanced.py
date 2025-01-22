# if_and_else_advanced_example1.py

def validate_registration(name, age, email):
    if not name.strip():
        print("Error: The name cannot be empty.")
    elif age <= 18:
        print("Error: You must be older than 18 to register.")
    elif not "@" in email or not "." in email:
        print("Error: The email is not valid.")
    else:
        print(f"Registration successful. Welcome, {name}!")

# Pruebas
validate_registration("", 20, "usuario@gmail.com")  # Error: The name cannot be empty.
validate_registration("Fabiola", 17, "usuario@gmail.com")  # Error: You must be older than 18 to register.
validate_registration("Carlos", 25, "usuariogmail.com")  # Error: The email is not valid.
validate_registration("Leon", 25, "usuario@gmail.com")  # Registration successful. Welcome, Carlos!
