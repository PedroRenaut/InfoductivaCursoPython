# comprueba_pass.py
# Comprueba si la contraseña es correcta.


contrasena_guardada = 'contrasena123'  # Cambia esto por la contraseña deseada

contrasena = input('Ingrese su contraseña: ')

if contrasena == contrasena_guardada:

    print('Contraseña correcta. Acceso permitido.')

else:

    print('Contraseña incorrecta. Acceso denegado.')

