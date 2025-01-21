def parse_formula(formula):
    elements = {}
    i = 0
    while i < len(formula):
        if formula[i].isupper():
            element = formula[i]
            i += 1
            if i < len(formula) and formula[i].islower:
                element += formula[i]
                i += 1
            count = ""
            while i < len(formula) and formula[i].isdigit:
                count += formula[i]
                i += 1
            if count == "":
                count = 1
            elements[element] = int(count)
        else:
            i += 1
    return elements