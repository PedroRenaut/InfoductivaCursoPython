# DNI
# version: 1.0

# Lista de letras correspondientes a los números del DNI
letras_dni = 'TRWAGMYFPDXBNJZSQVHLCKE'

# Solicitar al usuario su número de DNI o NIE
dni_numero = int(input('Introduce tu número de DNI o NIE (sin letra): '))

# Calcula la letra correspondiente
resto = dni_numero % 23
letra = letras_dni[resto]

# Imprime el número completo con la letra
print('Tu número completo es: ' + str(dni_numero) + letra)

