"""
Ejercicio 7
"""
nota_1 = float(input("Introduzca la nota 1: "))
nota_2 = float(input("Introduzca la nota 2: "))
nota_3 = float(input("Introduzca la nota 3: "))

promedio = (nota_1 + nota_2 + nota_3) / 3

nota_examen = float(input("Introduzca la nota del examen: "))

nota_trabajo = float(input("Introduzca la nota del trabajo: "))

nota_final = 0.55 * promedio + 0.30 * nota_examen + 0.15 * nota_trabajo

print(f"La nota final es {nota_final:.2f}")
