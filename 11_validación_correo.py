# Comprobar si un correo es válido o no

correo = input('Introduce tu correo electrónico: ')


for i in correo:
    if '@' in correo:
        print ('El correo es válido')
        break
    else:
        print ('El correo no es válido')
        break
        