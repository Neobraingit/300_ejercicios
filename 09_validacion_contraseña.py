
# Un programa que verifique si una contraseña cumple con los criterios

import re
import getpass

print ('La contraseña dene tener: 8 caracteres, mayúsculas, minúsculas y al menos un número.')

contraseña = getpass.getpass()

if len(contraseña) >= 8 and re.search(r'[a-z]', contraseña) and re.search(r'[A-Z]', contraseña) and re.search(r'[0-9]', contraseña):
    print ('Contraseña válida.')
else:
    print ('La contraseña no cumple con los criterios.')

