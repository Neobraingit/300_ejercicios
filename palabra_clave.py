# Un programa que determine el día de la semana correspondiente a una fecha ingresada

import datetime

def obtener_dia_semana(dia, mes, año):
    fecha = datetime.date(año, mes, dia)
    dia_semana = fecha.strftime('%A')
    return dia_semana
dia = int(input('Introduce el día: '))
mes = int(input('Introduce el mes: '))
año = int(input('Introduce el año: '))
dia_semana = obtener_dia_semana(dia,mes,año)
print ('El día de la semana es: ', dia_semana)