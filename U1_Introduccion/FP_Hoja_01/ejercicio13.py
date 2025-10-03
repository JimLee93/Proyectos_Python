"""
ejercicio 13
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta
llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la
ciudad B.
"""

horas = int(input("Introduzca las horas: "))
minutos = int(input("Introduzca los minutos: "))
segundos = int(input("Introduzca los segundos: "))
tiempo = int(input("Introduzca el tiempo en segundos: "))

horas_llegada = horas + (minutos + (segundos + tiempo) // 60) // 60
minutos_llegada = (minutos + (segundos + tiempo) // 60) % 60
segundos_llegada = (segundos + tiempo) % 60

print(f"La hora de llegada es {horas_llegada}:{minutos_llegada}:{segundos_llegada}")
