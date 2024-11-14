
''' Un programa que permita al usuario introducir calificaciones de alumnos y calcular el promedio'''

from colorama import Fore, Back, Style
import time

def calcular_promedio(calificaciones):
    total = sum(calificaciones)
    promedio = total/len(calificaciones)
    return promedio


calificaciones = []

while True:
    nota = float(input('Introduce una nota(-1 para terminar): '))
    if nota == -1:
        break
    calificaciones.append(nota)
    
    if calificaciones:
        promedio = calcular_promedio(calificaciones)
        print (Fore.RED +'El promedio de calificaciones es: ' + Style.RESET_ALL, promedio)
        time.sleep(2)
    else:
        print (Fore.BLUE + 'No se introdujeron notas' + Style.RESET_ALL)
    



    
    
