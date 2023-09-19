nota = 8

if nota < 5:
    print('Suspenso')
else:
    print('Aprobado')

# <4    MD
# <5    I
# <6    S
# <8    B
# <9    N
# >9    SB

if nota < 4:
    print('MD')
elif nota < 5:
    print('I')
elif nota < 6:
    print('S')
elif nota < 8:
    print('B')
elif nota < 9:
    print('N')
else:
    print('SB')

# Si la edad es inferior a 18 entonces...
# (A,B)
# Sino ...
# (C,D)
edad = 16
opcion = 'B'
if edad < 18:
    if opcion == 'A':
        print('A')
    elif opcion == 'B':
        print('B')
else:
    if opcion == 'C':
        print('C')
    elif opcion == 'D':
        print('D')

# Si la cesta de la compra es mayor a 50€ y además tiene la tarjeta de la tienda entonces... 2€ de descuento.
total = 58.25
tiene_trj = True

if total >= 50 and tiene_trj == True:
    print(f'Tienes descuento ... total a pagar {total - 2}')

# Ultima porción mejorada ... 
if total >= 50 and tiene_trj:
    print(f'Tienes descuento ... total a pagar {total - 2}')