from formula_parser import parse_formula

def calculate_molar_mass(formula):
    mass_table = {
        "H": 1.008, "O": 16.00, "C": 12.01, "N": 14.01
    }
    parsed = parse_formula(formula)#Utliziand la funcion de parseo para traer el diccionario y asi poder iterar con los valores de elemetn y count
    molar_mass = 0
    #for element, count in parsed:#aQUI NO ME REGRESA NADA 
    for element,count in parsed.items():
        if element not in mass_table: #Checando en el diccionario de mass table
            print(f"Error: Unknown element '{element}'.")#Si no esta en la tabla imprimir error
        else:#Le agregue un else para que no se calculara aunque no lo encontrara en la tabla
            molar_mass += mass_table[element] * count #va a sumar cada ves el resulado de multiplicar el valor de count por el valor que encontro en el mass table
    return molar_mass

print(calculate_molar_mass("H2O"))  # Output: 18.016
print(calculate_molar_mass("CH4"))  # Output: 16.04
