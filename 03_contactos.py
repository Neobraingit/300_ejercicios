
'''Crea un programa que permita al usuario registrar contactos con nombre, número de teléfono y correo.
Luego, permite al usuario buscar y mostrar la información de un conracto por nombre'''

contactos = {}

def agregar_contactos():
    nombre = input('Nombre: ')
    telefono = input('Teléfono: ')
    correo = input('Correo: ')
    contactos[nombre] = {'Teléfono': telefono, 'Correo': correo}
    print ('Contacto agregado.')
    
def buscar_contacto():
    nombre = input('Buscar por nombre: ')
    if nombre in contactos:
        print ('Información del contacto: ')
        print ('Nombre: ', nombre)
        print ('Teléfono: ', contactos[nombre]['Teléfono'])
        print ('Correo electrónico', contactos[nombre]['Correo'])
    else:
        print ('Contacto no encontrado.')
        
while True:
    print ('\nOpciones: ')
    print ('1.Agregar contacto')
    print ('2.Buscar contacto')
    print ('3.Salir')
    
    opcion = input('Selecciona una opción: ')
    
    if opcion == '1':
        agregar_contactos()
    elif opcion == '2':
        buscar_contacto()
    elif opcion == '3':
        break
    else:
        print ('Opción no válida.')
        
        