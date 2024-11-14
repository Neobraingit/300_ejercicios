from colorama import Fore, Back, Style
from tqdm import tqdm
import time
import os

cuenta_atrás = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in tqdm(cuenta_atrás, desc='Progreso: '):
    print (i)
    time.sleep(0.5)
    


tareas = []
def agregar_tarea ():
     tarea = input('Introduce una nueva tarea: ')
     tareas.append(tarea)
     print (Fore.YELLOW + 'Las tareas que quedan son: ', tareas, Style.RESET_ALL)
     
def completar_tarea ():
    tarea_completada = input('Introduce la tarea completada: ')
    for i in tareas:
        if tarea_completada in tareas:
            print (Fore.RED + 'Tarea marcada como completada.')
            print (Fore.YELLOW + 'La tarea completada es: ',tarea_completada,Style.RESET_ALL)
            tareas.remove(tarea_completada)
            print ('Las tareas que quedan son: ',tareas)
    
    
while True:
    print ('Escoge una opción: \n')
    print ('1. Agregar tarea\n')
    print ('2. Completar tarea\n')
    print ('3. Salir')
    opcion = input()
    if opcion == '1':
        agregar_tarea()
    elif opcion == '2':
            completar_tarea()
    elif opcion == '3':
        print (Fore.RED + 'Saliendo del programa...')
        time.sleep(2)
        break
    else:
        print ('Opción no válida.')
        
os.system('clear')
            
            

    