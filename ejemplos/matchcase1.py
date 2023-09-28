# Sentencia Condicional match-case
# Ejemplo 1

color = '#AABB00'

match color:
    case '#000000':
        print('Negro')

    case '#FFFFFF':
        print('Blanco')

    case '#FF0000':
        print('Rojo')

    case '#00FF00':
        print('Verde')

    case '#0000FF':
        print('Azul')

    case _:
        print('Color desconocido')

    

    