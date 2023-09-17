# DNI
# version: 2.0

# Lista de letras correspondientes a los números del DNI
letras_dni = 'TRWAGMYFPDXBNJZSQVHLCKE'

# Solicitar al usuario su número de DNI o NIE
dni_numero = int(input('Introduce tu número de DNI o NIE (sin letra): '))

# Calcula la letra correspondiente
letra = letras_dni[dni_numero % 23]

# Imprime el número completo con la letra
print(f'Tu número completo es: {dni_numero}{letra}')

