# Se declara una lista llamada colores que contiene varios nombres de colores.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

# Se elimina el elemento en la posición 1 de la lista (que es 'azul')
del colores[1]

# Se elimina el elemento en la posición 3 de la lista (que después de la primera eliminación es 'amarillo')
del colores[3]

# Se elimina el elemento en la posición 4 de la lista (que después de las eliminaciones anteriores es 'lila')
del colores[4]

# Se elimina el tercer elemento desde el final de la lista (que es 'blanco')
del colores[-3]

# Se imprime la lista resultante después de todas las eliminaciones
print(colores)
