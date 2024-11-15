from colorama import Fore,Back,Style

'''Un programa que permita calcular el precio final de un producto después de aplicarle un descuento'''

precio_producto = float(input('Introducce el precio del producto: '))
descuento = float(input('Introduce el descuento a aplicar: '))

def calcular_precio_final():
    precio_final = precio_producto / descuento
    print (Fore.RED + 'El precio final es: ' , precio_final)
    
    
palabra_clave = input('Escribe la palabra calcular para comenzar el proceso: ')
if palabra_clave == 'calcular':
    calcular_precio_final()

