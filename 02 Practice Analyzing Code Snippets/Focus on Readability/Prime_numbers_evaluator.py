def is_it_prime(num):#Cambiaria el nombre a pregunta: is_it_prime(num)
    """Verifica si un número es primo."""
    if (num <= 1):#Aqui evaluamos si el numero es uno o menor y enseguida decidimos que no es primo
        return print(f"El numero {num} NO es primo")
    for i in range(2, int(num**0.5) + 1): #En este for evaluamos si el numero es multiplo de 2 hasta la raiz cuadrada de num y le sumamos 1 para mantenernos dentreo del rango l
        if num % i == 0:#no vale la pena comparar con 1 porque todos los numeros son multiplos de uno
            return print(f"El numero {num} NO es primo")
        else:
            return print(f"El numero {num} SI es primo")

# Ejemplo de uso
print("¿Es primo?", is_it_prime(8))
