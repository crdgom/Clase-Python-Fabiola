def validate_database_entry(name, age, email, user_id):
    if len(nama) < 3 or not isinstance(name, str):
        print("Error: Name must be a string with at least three characters.")
    elif not isinstance(age, str) and age > 0:
        print("Error: Age must be a positive integer.")
    elif len(str(user_id)) != 8 or str(user_id).isalpha():
        print("Error: User ID must be an 8-digit number.")
    else:
        print(f"Valid entry: {name}, {age}, {email}, {user_id}")

# Test cases
validate_database_entry("John", 25, "john@example.com", "12345678")  # Valid entry
validate_database_entry("Jo", "25", "jo.com", "1234abcd")     