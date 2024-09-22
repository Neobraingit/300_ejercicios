
'''
Crea un programa que permita registrar usuarios y buscarlos. 
'''

contactos = {}

def agregar_contacto():
    nombre = input('Nombre: ')
    telefono = input('Teléfono: ')
    correo = input('Correo electrónico: ')
    contactos[nombre] = {'Teléfono': telefono, 'Correo': correo}
    print ('Contacto agregado')
    
def buscar_contacto():
    nombre = input('Buscar contacto por nombre: ')
    if nombre in contactos:
        print ('Información del contacto:')
        print ('Nombre:', nombre)
        print ('Teléfono:', contactos[nombre]['Teléfono'])
        print ('Correo electrónico:', contactos[nombre]['Correo'])
        
    else:
        print ('Contacto no encontrado')
        
while True:
    print ('\nOpciones:')
    print ('1. Agregar contacto')
    print ('2.Buscar contacto')
    print ('3.Salir')
    
    opcion = input('Selecciona una opción: ')
    
    if opcion == '1':
        agregar_contacto()
    elif opcion == '2':
        buscar_contacto()
    elif opcion == '3':
        break
    else:
        print ('Opción no válida')