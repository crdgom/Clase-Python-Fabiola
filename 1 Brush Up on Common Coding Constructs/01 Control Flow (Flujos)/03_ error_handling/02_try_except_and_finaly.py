def process_input(data):
    try:
        number = int(data)
        result = 10 / number
    except ValueError:
        print("Error: Input must be a number.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Processed result: {result}")

# Test cases
process_input("5")
process_input("abc")
process_input("0")