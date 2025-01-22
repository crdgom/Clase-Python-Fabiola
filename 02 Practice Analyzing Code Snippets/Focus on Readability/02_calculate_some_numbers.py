def calculate_average(numbers):
    """Calcula el promedio de una lista de números."""
    if not numbers:
        return "La lista está vacía."
    return sum(numbers) / len(numbers)

# Ejemplo de uso
print("Promedio:", calculate_average([10, 20, 30, 40, 50]))
