
'''
Crea un programa que permita al usuario introducir calificaciones y calcular el promedio. 
'''
calificaciones = []

def introducir_calificaciones():
    nota = int(input('Introduce la nota del alumno: '))
    calificaciones.append(nota)
    print (calificaciones)
    
def promedio_calificaciones():
    suma = sum(calificaciones)
    print ('La suma de todas las notas es de: ', suma) 
    print ('El promedio de todas las calificaciones es de: ', suma/len(calificaciones)) 
    

    
while True:
    print ('Opciones\n')
    print ('1. Introducir nota\n')
    print ('2. Calcular promedio\n')
    print ('3. Salir\n')
    opcion = input('Introduce la opción: ')
    if opcion == '1':
        introducir_calificaciones()
    elif opcion == '2': 
        promedio_calificaciones()
    elif opcion == '3':
        break
    else: 
        print ('Opción no válida.')

    