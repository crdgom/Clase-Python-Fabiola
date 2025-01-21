age = -1

while age < 1 or age > 120:
    age = input("Enter a valid age between 1 and 120: ")
    if not age.isdigit():
        print("Error: Age must be a number.")
        continue
    age = int(age)

print(f"Valid age entered: {age}")