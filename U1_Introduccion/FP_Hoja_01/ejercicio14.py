"""
Ejercicio 14
Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
Ten en cuenta que las iniciales pueden ser mayúsculas o minúsculas
No se puede dejar vacio el nombre y los apellidos al pedirlos
"""
NOMBRE=""
APELLIDO1=""
APELLIDO2=""
while not NOMBRE.strip():
    NOMBRE = input("Introduzca su nombre: ")
    NOMBRE = NOMBRE.strip()
while not APELLIDO1.strip():
    APELLIDO1 = input("Introduzca su primer apellido: ")
    APELLIDO1 = APELLIDO1.strip()
while not APELLIDO2.strip():
    APELLIDO2 = input("Introduzca su segundo apellido: ")
    APELLIDO2 = APELLIDO2.strip()

print(f"Las iniciales son {NOMBRE[0].upper()}.{APELLIDO1[0].upper()}.{APELLIDO2[0].upper()}")
