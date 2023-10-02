# Ejemplos de utilización del bucle while

# Ejemplo 1
num = 1
while num <= 10:
    print(num)
    num += 1

# Ejemplo 2
valor = 1
while valor >= 1:
    if valor % 5 == 0:
        break
    valor += 1
print(valor)

# Ejemplo 3
valor = 0
while valor <= 50:
    valor += 1
    if valor % 5 == 0:
        print(f'{valor} es multiplo de 5')
        continue
    print(valor)
    
