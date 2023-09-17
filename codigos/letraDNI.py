def calcular_letra_dni(dni_numero):
    # Lista de letras correspondientes a los números del DNI
    letras_dni = 'TRWAGMYFPDXBNJZSQVHLCKE'
    
    # Calcula la letra correspondiente
    letra = letras_dni[dni_numero % 23]
    
    return letra

def main():
    try:
        # Solicitar al usuario su número de DNI o NIE
        dni_numero = int(input('Introduce tu número de DNI o NIE (solo números): '))
        
        if dni_numero < 0 or dni_numero > 99999999:
            print('Número de DNI o NIE no válido. Debe estar entre 0 y 99999999.')
        else:
            # Calcula la letra correspondiente
            letra = calcular_letra_dni(dni_numero)
            
            # Imprime el número completo con la letra
            print(f'Tu número completo es: {dni_numero}{letra}')
    except ValueError:
        print('Error: Introduce un número válido.')

if __name__ == "__main__":
    main()