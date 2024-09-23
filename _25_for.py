#!/usr/bin/env python
# _*_ coding: cp1252  _*_
# _*_ coding: 850  _*_
# _*_ coding: utf-8  _*_
# Tupla de colores
colores = ('rojo', 'azul', 'verde', 'amarillo', 'negro')

# Bucle for que itera sobre cada color en la tupla
for color in colores:
    # Si el color es 'verde', se salta esta iteración
    if color == 'verde':
        print('Se saltó el color:', color)
        continue

    # Si el color es 'negro', se rompe el bucle
    if color == 'negro':
        print('Se rompió el bucle en el color:', color)
        break

    # Imprime la frase para los colores restantes
    print('El color es:', color + '.')

