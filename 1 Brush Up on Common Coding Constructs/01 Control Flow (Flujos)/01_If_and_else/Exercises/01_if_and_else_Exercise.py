"""
? Objetivo: Pedir un número al usuario (usando input()) e imprimir si es mayor que 10 o no.
 TODO Ejercicio: Ejercicio 1:
 TODO  - Objetivos: Tener conciencia de PEP 8 y el control de flujo SI (IF) y SINO (ELSE)
"""

def ejercicio1():
#* Comenzamos pidiendo el número:
 numero = input("Ingresa un número: ")

#* Acá tenemos el primer control de flujo (el más basico con dos sentencias si)
#* SI el numero es mayor que 10 devolvemos (el numero es mayor que 10)
if numero > 10:
print("Es mayor que 10")

#* SINO es mayor que 10 devolvemos (No es mayor que 10)
else:
print("No es mayor que 10")