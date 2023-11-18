# Ejemplos de listas Python

lista_vacia = []

idiomas = ['Español','Francés','Inglés','Italiano']

numeros = [1,5,3,1,2,4,9]

datos = ['Madrid', {'cielo':'despejado','temp':15}, 604.3, (-3.7025600, 40.4165000)]

# nombre = 'Pedro'
# print(list(nombre))

# print(list(reversed(idiomas)))
# print(idiomas)

# idiomas.reverse()
# print(idiomas)

# idiomas.append('Griego')
# print(idiomas)

'''for num in range(20):
    if num % 2 == 0:
        lista_vacia.append(num)

print(lista_vacia)'''

'''idiomas.insert(1, 'Portugués')
idiomas.insert(200, 'Alemán')
print(idiomas)'''

# print(idiomas * 2)

#print(idiomas + numeros)

# idiomas.extend(numeros)
# print(idiomas)
# print(numeros)

# idiomas.extend('Sueco')
# print(idiomas)

# numeros[0:3] = [8,8]
# print(numeros)

'''print(idiomas)
del(idiomas[1])
print(idiomas)'''

'''print(idiomas)
idiomas.remove('Francés')
print(idiomas)'''

'''print(idiomas)
print(idiomas.pop(2))
print(idiomas)'''

'''print(idiomas)
idiomas[1:3] = []
print(idiomas)'''

'''print(idiomas)
#idiomas.clear()
idiomas = []
print(idiomas)'''

# print(idiomas)
# print(idiomas.index('Inglés'))

# print('Ingles' in idiomas)

# print(numeros.count(15))
# print(idiomas.count('Ruso'))

#print('-'.join(idiomas))
'''cadena_texto = '*'.join(idiomas)
print(cadena_texto)'''

#print('-'.join(numeros))
'''print(numeros)
print(sorted(numeros))
print(numeros)'''

'''print(numeros)
numeros.sort()
print(numeros)'''

#print(sorted(numeros, reverse = True))

'''idiomas.sort(reverse=True)
print(idiomas)'''

# print(len(numeros))

'''for num, idioma in enumerate(idiomas):
    print(num+1, idioma)
'''

'''nombres = ['Antonio', 'Luis', 'Juan']
apellidos = ['Ruiz','López','Jarandilla']

for nombre, apellido in zip(nombres, apellidos):
    print(nombre, apellido)

print(list(zip(nombres,apellidos)))'''

'''original = [1,2,3,4,5,6]
#copia = original
copia = original.copy()

original[0] = 10
print(original)
print(copia)'''

