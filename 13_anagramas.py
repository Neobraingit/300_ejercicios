# Un programa que determine si dos palabras son anagramas

palabra_1 = input('Introduce una palabra: ')
palabra_2 = input('Introduce una segunda palabra: ')

if sorted(palabra_1) == sorted(palabra_2):
    print ('Las palabras son anagramas.')
else:
    print ('Las palabras no son anagramas')