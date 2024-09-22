'''
Crea un programa que calcule el IMC de una persona a partir de su peso y la altura. 
Luego muestra si es una de las soguientes categorías (bajo peso, peso normal, sobrepeso)
'''

altura = float(input('Dime tu altura: '))
peso = float(input('Dime tu peso: '))
imc = (altura * 2) / peso

print (f'Tu índice de masa corporal es: {imc}')

if peso <= 80:
    print ('Estás en tu peso')
elif peso > 80 and  peso<= 100:
    print ('Estás gord@')
elif peso> 100:
    print ('Tienes sobrepeso')
    
    