# calcula_IMC.py
# Calcula el Indice de Masa Corporal (IMC)..

print('Calculadora de IMC - Índice de Masa Corporal')

peso = float(input('Ingrese su peso en kilogramos: '))

altura = float(input('Ingrese su altura en metros: '))

imc = peso / (altura ** 2)

print('Su IMC es:', imc)

if imc < 18.5:

    print('Está bajo peso')95

elif imc < 24.9:

    print('Su peso es normal')

elif imc < 29.9:

    print('Tiene sobrepeso')

else:

    print('Tiene obesidad')

