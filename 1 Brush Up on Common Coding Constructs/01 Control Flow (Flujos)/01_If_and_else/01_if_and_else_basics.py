"""
#TODO en este ejercicio Repasaremos 1 operador de Asignación (=)
#TODO y 2 Operadores relacionales.
#TODO Tambien PEP8 (Estilos de codificación de Python, convenciones y
#   buenas practicas).
"""
def basic_example_if_else(number):
        """
        ? Ejemplo básico de if-else.
        TODO Determina si un número es positivo, negativo o cero.
        """
        #* Creamos la variable Numero y le asigmanos el valor 0
        #numero = 0 #* variable privada (LOCAL)

        if number  > 0:
            print("El número es positivo.")
        elif number < 0:
            print("El número es negativo.")
        else:
            print("El número es cero.")

#? Caso1
basic_example_if_else(10)


#? Caso2

#basic_example_if_else(-5)

#? Caso3

#basic_example_if_else(0)
    