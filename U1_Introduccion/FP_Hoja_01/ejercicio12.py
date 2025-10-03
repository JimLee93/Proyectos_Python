"""
Ejercicio 12
"""

distancia = int(input("Introduzca la distancia (km): "))
velocidad_1 = int(input("Introduzca la velocidad 1 (km/h): "))
velocidad_2 = int(input("Introduzca la velocidad 2 (km/h): "))

tiempo = distancia / (velocidad_1 - velocidad_2)

print(f"El tiempo es {tiempo} minutos")
