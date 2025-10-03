"""
Ejercicio 15
Escribir un algoritmo para calcular la nota final de un estudiante, considerando que por cada respuesta
correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido
por el estudiante.
"""
def calcular_nota(respuestas_correctas, respuestas_incorrectas, respuestas_en_blanco):
    """
    Calcula la nota final de un estudiante basado en las respuestas correctas, incorrectas 
    y en blanco.
    5 puntos por cada respuesta correcta, -1 por cada respuesta incorrecta, 
    y 0 por respuestas en blanco.
    Parámetros:
    respuestas_correctas (int): Número de respuestas correctas.
    respuestas_incorrectas (int): Número de respuestas incorrectas.
    respuestas_en_blanco (int): Número de respuestas en blanco.
    Retorna:
    int: Nota final del estudiante.
    """
    nota = (respuestas_correctas * 5) + (respuestas_incorrectas * -1) + (respuestas_en_blanco * 0)
    return nota
def main():
    """
    Función principal para ejecutar el cálculo de la nota final.
    Solicita al usuario el número de respuestas correctas, incorrectas y en blanco,
    y muestra la nota final calculada.
    """
    print("Calculadora de nota final de un estudiante")
    respuestas_correctas = int(input("Ingrese el número de respuestas correctas: "))
    respuestas_incorrectas = int(input("Ingrese el número de respuestas incorrectas: "))
    respuestas_en_blanco = int(input("Ingrese el número de respuestas en blanco: "))
    nota_final = calcular_nota(respuestas_correctas, respuestas_incorrectas, respuestas_en_blanco)
    print(f"La nota final del estudiante es: {nota_final}")
