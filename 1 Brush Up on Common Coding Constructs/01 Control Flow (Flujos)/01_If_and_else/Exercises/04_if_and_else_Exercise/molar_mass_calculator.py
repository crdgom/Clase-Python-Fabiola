from formula_parser import parse_formula

def calculate_molar_mass(formula):
    mass_table = {
        "H": 1.008, "O": 16.00, "C": 12.01, "N": 14.01
    }
    parsed = parse_formula(formula)
    molar_mass = 0
    for element, count in parsed:
        if element not in mass_table:
            print(f"Error: Unknown element '{element}'.")
        molar_mass += mass_table[element] * count
    return molar_mass

# Test case
print(calculate_molar_mass("H2O"))  # Output: 18.016
print(calculate_molar_mass("CH4"))  # Output: 16.04