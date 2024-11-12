
'''Programa que permita al usuario convertor Celsius a Fahrenheit o viceversa'''

celsius = int(input('Introduce los grados celsius: '))
fahrenheit = int(input('Introduce los grados fahrenheit: '))

convertir_a_celsius = (fahrenheit * 9/5) + 32
convertir_A_fahrenheit = (celsius -32) * 5/9


print (f'La temperatura en celsius es {convertir_a_celsius}')
print (f'La temperatura en Fahrenheit es {convertir_A_fahrenheit}')