#!/usr/bin/env python
# _*_ coding: cp1252  _*_
# _*_ coding: 850  _*_
# _*_ coding: utf-8  _*_
# Inicializamos la variable x en 0
x = 0

# Bucle while con condici�n de salida cuando x sea mayor o igual a 30
while x < 30:
    x += 1  # Incremento de 1 en cada iteraci�n

    # Comprobamos si x es uno de los valores que debemos saltar
    if x == 4 or x == 6 or x == 10:
        print('Se salt� el valor', x, 'de x')
        continue  # Salta la ejecuci�n del resto del bucle y pasa a la siguiente iteraci�n

    # Rompemos la ejecuci�n si x vale 15
    if x == 15:
        print('Se rompi� la ejecuci�n del bucle cuando x val�a:', x)
        break

    # Imprime el valor del bucle
    print('El valor del bucle es:', x)

