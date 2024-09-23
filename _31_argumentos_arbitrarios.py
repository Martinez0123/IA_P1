#!/usr/bin/env python
# _*_ coding: cp1252  _*_
# _*_ coding: 850  _*_
# _*_ coding: utf-8  _*_
def libro(titulo, autor, *args):  # Definimos la función libro con parámetros adicionales
    print('El título del libro es:', titulo)  # Imprime el título del libro
    print('El autor del libro es:', autor)    # Imprime el autor del libro
    for x in args:  # Itera sobre los argumentos adicionales (años de publicación)
        print('Año de publicación:', x)  # Imprime cada argumento adicional (año de publicación)

# Lista de años de publicación
años_publicacion = [2001, 2005, 2010]

# Llamada a la función libro con el título, el autor y los años de publicación
libro('Cien años de soledad', 'Gabriel García Márquez', *años_publicacion)

