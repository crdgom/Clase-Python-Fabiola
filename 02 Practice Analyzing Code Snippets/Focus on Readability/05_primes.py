def is_prime(num):
    """Verifica si un número es primo."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Ejemplo de uso
print("¿Es primo?", is_prime(17))
