# -*- coding: utf-8 -*-
"""ejemplos

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xa8Ql9yjjcdnu6YRynXQPjc03BerjGRl
"""

def find_combination(lista, objetivo):
    inicio = 0
    suma_actual = lista[0]
    combinaciones = []

    for fin in range(1, len(lista) + 1):
        while suma_actual > objetivo and inicio < fin - 1:
            suma_actual -= lista[inicio]
            inicio += 1

        if suma_actual == objetivo:
            combinacion_actual = lista[inicio:fin]
            if not combinaciones or len(combinacion_actual) < len(combinaciones[0]):
                combinaciones = [combinacion_actual]
            elif len(combinacion_actual) == len(combinaciones[0]):
                combinaciones.append(combinacion_actual)

        if fin < len(lista):
            suma_actual += lista[fin]

    if combinaciones:
        for combinacion in combinaciones:
            print(f"Combinación encontrada: {combinacion}")
    else:
        print("No existe una combinación")

# Ejemplo de uso:
numeros = [6, 2, 8, 5, 9, 1, 7, 4, 1]
objetivo = 14

find_combination(numeros, objetivo)

def longitud_string_mas_largo(s):
    # Dividir el string en partes de no más de 2 caracteres
    partes = [s[i:i+2] for i in range(0, len(s), 2)]

    # Encontrar la longitud del string más largo entre las partes
    max_longitud = max(len(part) for part in partes)

    return max_longitud

# Ejemplo de uso
input_string = input("Ingrese un string: ")
resultado = longitud_string_mas_largo(input_string)
print(f"La longitud del string más largo con no más de 2 caracteres es: {resultado}")

def longitud_substring_distinto(s):
    if not s:
        return 0

    max_longitud = 1  # Inicializamos con un substring de un solo carácter
    longitud_actual = 1

    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            longitud_actual += 1
        else:
            longitud_actual = 1

        max_longitud = max(max_longitud, longitud_actual)

    return max_longitud

# Ejemplo de uso
input_string = input("Ingrese un string: ")
resultado = longitud_substring_distinto(input_string)
print(f"La longitud del substring más largo con caracteres consecutivos distintos es: {resultado}")