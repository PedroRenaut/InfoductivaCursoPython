# Solicitar al usuario que ingrese dos números
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

# Verificar si los valores ingresados son números válidos
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Uno o ambos valores no son números válidos.")
    exit(1)

# Solicitar al usuario que elija una operación
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Validar la selección de operación del usuario
operacion = input("Elija una operación (1/2/3/4): ")

if operacion not in ('1', '2', '3', '4'):
    print("Selección no válida.")
    exit(1)

# Realizar la operación seleccionada y mostrar el resultado
if operacion == '1':
    resultado = num1 + num2
    print("Resultado: ", resultado)
elif operacion == '2':
    resultado = num1 - num2
    print("Resultado: ", resultado)
elif operacion == '3':
    resultado = num1 * num2
    print("Resultado: ", resultado)
elif operacion == '4':
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
        exit(1)
    resultado = num1 / num2
    print("Resultado: ", resultado)