# DNI
# version: 3.0

letras_dni = 'TRWAGMYFPDXBNJZSQVHLCKE'

dni_numero = int(input('Introduce tu número de DNI o NIE (sin letra): '))

letra = letras_dni[dni_numero % 23]

print(f'Tu número completo es: {dni_numero}{letra}')