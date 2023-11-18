# Ejemplo de Listas por compresión
valores = '53,51,11,19'

valores_int = []

for valor in valores.split(','):
    valor_int = int(valor)
    valores_int.append(valor_int)

print(f'Resultado: {valores_int}\n\n')

# Equivalente con lista de compresión.
# Estructura:
# [<expresión>      for <valor> in <iterable>       if <condición>]
"""
    valor de            Itera/Genera valores        Filtrado de
    cada elemento                                   valores
    de la nueva
    lista
"""
valores_int = [int(valor) for valor in valores.split(',')]
print(f'Resultado: {valores_int}\n\n')

# Condición en compresión
valores_int = [int(v) for v in valores.split(',') if v.startswith('5')]
print(f'Resultado: {valores_int}\n\n')

# Bucles anidados en compresiones.
valores = '53,51,11,19'
svalores = valores.split(',')
combinaciones = [f'{v1}x{v2}' for v1 in svalores for v2 in svalores]
print(combinaciones)

# sum() ... max() ... min()
valores = [53,51,11,19]
print(f'Suma = {sum(valores)}')
print(f'Min  = {min(valores)}')
print(f'Max  = {max(valores)}')