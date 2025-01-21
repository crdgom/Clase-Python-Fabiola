def switch_case(argument):
    switcher = {
        0: "January",
        1: "February",
        2: "March",
    }
    return switcher.get(argument, "Invalid month")  

print(switch_case(0))
print(switch_case(1))
print(switch_case(2))
print(switch_case(3))