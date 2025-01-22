# crearemos un programa que pida el input de un numero a un usuario y que nos devuelva si es par o impar.

def is_even_or_odd():

    number = int(input(">>> Enter a number: "))

    if number %2 == 0:
        return print("The number is even.")
    else:
        return print("The number is odd.")
    
is_even_or_odd()