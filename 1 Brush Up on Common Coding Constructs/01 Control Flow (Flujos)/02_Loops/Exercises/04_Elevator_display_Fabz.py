building_floors = 100
current_floor = 1

"""while current_floor <= building_floors:
    print(f"Ascending to floor {current_floor}")
    current_floor += 1

print("Reached the top floor!")
"""

while True:
    print(f"Ascending to floor {current_floor}")
    current_floor +=1 
    if (current_floor == building_floors):
        print("Reached the top floor!")
        break
