
'''
Escribe un programa que pase Celsius a Fahrenheit o viceversa. 
'''




def celsius_a_fahrenheit():
    grados_celsius = float(input('Introduce los grados Celsius: '))
    resultado = grados_celsius * 9**5 * 32
    print (resultado)
    
def fahrenheit_a_celsius():
    grados_fahrenheit = float(input('Introduce los grados Fahrenheit: '))
    resultado2 = grados_fahrenheit - 32 * 0.5556
    print (resultado2)
    
print ('--- Menú ---\n')
print ( '1) Pasar Celsius a Fahrenheit\n')
print ( '2) Pasar Fahrenheit a Celsius ')
opcion =  input('\nIntroduce tu opción: ')

if opcion == '1':
    celsius_a_fahrenheit()
elif opcion == '2':
    fahrenheit_a_celsius()

