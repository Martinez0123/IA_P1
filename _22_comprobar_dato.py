#!/usr/bin/env python
# _*_ coding: cp1252  _*_
# _*_ coding: 850  _*_
# _*_ coding: utf-8  _*_

# Se declara una tupla con cuatro colores
colores_admitidos = ('rojo', 'azul', 'verde', 'amarillo')

# Se solicita al usuario que ingrese un color
color_usuario = input('Introduce un color:\n')

# Condiciones para cada color usando el operador 'in'
if 'rojo' in color_usuario:
    print('El color rojo est� admitido.')
elif 'azul' in color_usuario:
    print('El color azul est� admitido.')
elif 'verde' in color_usuario:
    print('El color verde est� admitido.')
elif 'amarillo' in color_usuario:
    print('El color amarillo est� admitido.')
else:
    print('Color no admitido.')

