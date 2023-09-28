# Sentencia Condicional match-case
# Ejemplo 3

dimensiones = ('10', '3', '7')

match dimensiones:
    case (int(), int()):
        print(f'({dimensiones}) es un plano en 2 dimensiones.')

    case (int(), int(), int()):
        print(f'({dimensiones}) es un plano en 3 dimensiones.')

    case _:
        print('Dimensión desconocida.')

