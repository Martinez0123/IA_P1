#!/usr/bin/env python
# _*_ coding: cp1252  _*_
# _*_ coding: 850  _*_
# _*_ coding: utf-8  _*_



edad = int(input('¿Cual es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad > 18 and edad <= 45:
	print('Eres mayor de edad.')
elif edad > 45 and edad <= 100:
	print('Eres mayor de edad, pero ya no tan joven.')
elif edad > 100 and edad <= 120:
	print('Eres muy mayor.')
else:
	print('Edad no valida.')