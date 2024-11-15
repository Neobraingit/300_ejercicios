
# Un programa que genere contraseña seguras. El usuario escoge la longitud.

import random
import string

longitud = int(input('Longitud de la contraseña: '))
caracteres = string.ascii_letters + string.digits + string.punctuation
contraseña = "".join(random.choice(caracteres)for _ in range(longitud))
print ('Contraseña generada: ', contraseña)