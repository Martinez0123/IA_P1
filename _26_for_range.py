#!/usr/bin/env python
# _*_ coding: cp1252  _*_
# _*_ coding: 850  _*_
# _*_ coding: utf-8  _*_

# Inicializaci�n de variables para almacenar la suma total, pares e impares
suma_total = 0
pares = 0
impares = 0

# Bucle for que itera sobre un rango de n�meros del 1 al 20
for numero in range(1, 21):
    # Sumar cada n�mero al total
    suma_total += numero

    # Comprobar si el n�mero es par o impar
    if numero % 2 == 0:
        pares += 1
        print(f'El n�mero {numero} es par.')
    else:
        impares += 1
        print(f'El n�mero {numero} es impar.')

# Mostrar los resultados finales
print("\nResultados finales:")
print(f'La suma total de los n�meros del 1 al 20 es: {suma_total}')
print(f'Cantidad de n�meros pares: {pares}')
print(f'Cantidad de n�meros impares: {impares}')
