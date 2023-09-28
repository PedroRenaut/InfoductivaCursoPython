# Sentencia Condicional match-case
# Ejemplo 2

dimensiones = (10, 3, 7)

match dimensiones:
    case (x, y):
        print(f'({x},{y}) es un plano en 2 dimensiones.')

    case (x, y, z):
        print(f'({x},{y},{z}) es un plano en 3 dimensiones.')

