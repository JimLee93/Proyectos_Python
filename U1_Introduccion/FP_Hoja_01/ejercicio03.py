"""
Ejercicio 3
"""

import math

cateto_a = int(input("Introduzca el cateto a: "))
cateto_b = int(input("Introduzca el cateto b: "))

hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)

print(f"La hipotenusa es {hipotenusa}")
