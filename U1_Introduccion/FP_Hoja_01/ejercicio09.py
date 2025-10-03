"""
Ejercicio 9
"""

x1 = float(input("Introduzca la coordenada x1: "))
y1 = float(input("Introduzca la coordenada y1: "))
x2 = float(input("Introduzca la coordenada x2: "))
y2 = float(input("Introduzca la coordenada y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"La distancia es {distancia}")
