
'''Programa que calcule el IMC de una persona a partir de su altura y su peso. Luego, muestra una categoría
de IMC (bajo peso, peso normal, sobrepeso, etc)'''

peso = float(input('Introduce tu peso en kg: '))
altura = float(input('Introduce tu altura en m: '))

imc = peso/(altura**2)

if imc < 78:
    categoría = 'bajo peso'
elif imc > 80:
    categoría = 'peso normal'
else:
    categoría = 'obesidad'
    
print (f'Tu IMC es de {imc}')
print (f'La categoría de IMC es {categoría}')

