"""
Ejercicio 6
"""
sueldo_base = float(input("Introduzca el sueldo base: "))
ventas = float(input("Introduzca la cantidad de ventas: "))
comision = 10/100 * ventas
sueldo_total = sueldo_base +  comision

print(f"El sueldo total es {sueldo_total}, comisión {comision}")
