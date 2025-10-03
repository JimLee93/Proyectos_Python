"""
Ejercicio 11
Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que
intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
"""
numA = int(input("Introduzca el primer número: "))
numB = int(input("Introduzca el segundo número: "))

numA, numB = numB, numA

print(f"El primer número es {numA} y el segundo número es {numB}")
