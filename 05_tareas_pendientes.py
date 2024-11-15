from colorama import Fore, Back, Style
from tqdm import tqdm
import time
import os

print ('\n','''888888    db    88""Yb 888888    db    .dP"Y8     88""Yb 888888 88b 88 8888b.  88 888888 88b 88 888888 888888 .dP"Y8 
  88     dPYb   88__dP 88__     dPYb   `Ybo."     88__dP 88__   88Yb88  8I  Yb 88 88__   88Yb88   88   88__   `Ybo." 
  88    dP__Yb  88"Yb  88""    dP__Yb  o.`Y8b     88"""  88""   88 Y88  8I  dY 88 88""   88 Y88   88   88""   o.`Y8b 
  88   dP""""Yb 88  Yb 888888 dP""""Yb 8bodP'     88     888888 88  Y8 8888Y"  88 888888 88  Y8   88   888888 8bodP''')

cuenta_atrás = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print ('Iniciando programa¡','\n')
for i in tqdm(cuenta_atrás, desc='Progreso: '):
    print (i)
    time.sleep(0.5)
    


tareas = []
def agregar_tarea ():
     tarea = input('Introduce una nueva tarea: ')
     tareas.append(tarea)
     print (Fore.YELLOW + 'Las tareas que quedan por completar son: ', tareas, Style.RESET_ALL)
     
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
            
            

    