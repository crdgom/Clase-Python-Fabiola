# crearemos un programa que pida el input de un numero a un usuario y que nos devuelva si es par o impar.

def is_even_or_odd():

    number = input(">>> Enter a number: ")

    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."
    
is_even_or_odd()