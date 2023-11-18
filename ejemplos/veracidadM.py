# Comprobar Veracidad Múltiple

# Comprueba que una palabra ... 
#   - tenga más de 4 caracteres de longitud
#   - empiece por r
#   - y contenga una a

# Ejemplo 1: Método Clásico

palabra = 'rayo'

"""if len(palabra) >= 4 and palabra.startswith('r') and palabra.count('a'):
    print('Palabra aceptada!')
else:
    print('Palabra Rechazada!!!!!!')"""

# Ejemplo 2: all()
palabra = 'bate'
longitud = len(palabra) >= 4
empieza = palabra.startswith('r')
contiene_a = palabra.count('a')

# veracidad = all([longitud,empieza,contiene_a])
veracidad = any([longitud,empieza,contiene_a])

if veracidad:
    print('Palabra aceptada!')
else:
    print('Palabra Rechazada!!!!!!')

