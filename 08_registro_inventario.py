
# Un programa que permita llevar un registro, con nombres, cantidades y mostrar el inventario actual

inventario = {}

def agregar_producto():
    producto = input('Nombre del producto: ')
    cantidad = int(input('Cantidad: '))
    inventario[producto] = cantidad
    print ('Producto agregado al inventario.')
    
def actualizar_cantidad():
    producto = input('Nombre del producto para actualizar: ')
    if producto in inventario:
        nueva_cantidad = int(input('Nueva cantidad: '))
        inventario[producto] = nueva_cantidad
        print ('Cantidad actualizada.')
    else:
        print ('Producto no encontrado en el inventario.')
        
def mostrar_inventario():
    for producto, cantidad in inventario.items():
        print (f'{producto}:{cantidad}')
        
while True:
    print ('\nOpciones: ')
    print ('1. Agregar al inventario')
    print ('2. Actualizar cantidad de un producto')
    print ('3. Mostrar inventario')
    print ('4. Salir')

    opcion = input('Selecciona una opción: ') 

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        actualizar_cantidad()
    elif opcion == '3':
            mostrar_inventario()  
    elif opcion == '4':
        quit()    
    else:
        print ('Opción no válida.')     
        