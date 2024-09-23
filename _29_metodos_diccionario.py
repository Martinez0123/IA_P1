#!/usr/bin/env python
# _*_ coding: cp1252  _*_
# _*_ coding: 850  _*_
# _*_ coding: utf-8  _*_
# Definimos dos productos de audio como diccionarios
auriculares1 = {
    'modelo': 'WH-1000XM4',
    'marca': 'Sony',
    'precio': '1750'
}

auriculares2 = {
    'modelo': 'QuietComfort 35 II',
    'marca': 'Bose',
    'precio': '9520'
}

# Eliminamos el precio del primer producto
del auriculares1['precio']

# Imprimimos el diccionario auriculares1 sin el precio
print("Información de auriculares1 después de eliminar el precio:")
print(auriculares1)

# Imprimimos el diccionario auriculares2 completo para comparar
print("\nInformación completa de auriculares2:")
print(auriculares2)
