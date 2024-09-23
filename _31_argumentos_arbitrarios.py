#!/usr/bin/env python
# _*_ coding: cp1252  _*_
# _*_ coding: 850  _*_
# _*_ coding: utf-8  _*_
def libro(titulo, autor, *args):  # Definimos la funci�n libro con par�metros adicionales
    print('El t�tulo del libro es:', titulo)  # Imprime el t�tulo del libro
    print('El autor del libro es:', autor)    # Imprime el autor del libro
    for x in args:  # Itera sobre los argumentos adicionales (a�os de publicaci�n)
        print('A�o de publicaci�n:', x)  # Imprime cada argumento adicional (a�o de publicaci�n)

# Lista de a�os de publicaci�n
a�os_publicacion = [2001, 2005, 2010]

# Llamada a la funci�n libro con el t�tulo, el autor y los a�os de publicaci�n
libro('Cien a�os de soledad', 'Gabriel Garc�a M�rquez', *a�os_publicacion)

