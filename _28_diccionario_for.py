#!/usr/bin/env python
# _*_ coding: cp1252  _*_
# _*_ coding: 850  _*_
# _*_ coding: utf-8  _*_
# Definimos varios productos de audio como diccionarios
auriculares1 = {
    'Categoría': 'Auriculares',
    'Modelo': 'Sony WH-1000XM4',
    'Precio': '4500'
}

auriculares2 = {
    'Categoría': 'Auriculares',
    'Modelo': 'Bose QuietComfort 35 II',
    'Precio': '2850'
}

altavoz1 = {
    'Categoría': 'Altavoces',
    'Modelo': 'JBL Flip 5',
    'Precio': '8000'
}

microfono1 = {
    'Categoría': 'Micrófonos',
    'Modelo': 'Blue Yeti',
    'Precio': '7500'
}

# Lista de todos los productos
productos = [auriculares1, auriculares2, altavoz1, microfono1]

# Iteramos sobre cada producto e imprimimos sus valores
for x, producto in enumerate(productos, 1):
    print(f"\nProducto {x}:")
    for clave in producto:
        print(producto[clave])
