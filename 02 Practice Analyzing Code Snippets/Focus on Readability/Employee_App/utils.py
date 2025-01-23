__version__ = '0.1'
__author__ = '@crdgom'

# Utility functions for input handling

def get_int_input(prompt):
    """Prompts the user for an integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_str_input(prompt):
    """Prompts the user for a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a valid value.")
