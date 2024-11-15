from ftplib import FTP
from tqdm import tqdm
import time
from colorama import Fore,Back,Style
import os
import shutil
import getpass

print (''' dP""b8  dP"Yb  88b 88 888888 Yb  dP 88  dP"Yb  88b 88     888888 888888 88""Yb 
dP   `" dP   Yb 88Yb88 88__    YbdP  88 dP   Yb 88Yb88     88__     88   88__dP 
Yb      Yb   dP 88 Y88 88""    dPYb  88 Yb   dP 88 Y88     88""     88   88"""  
 YboodP  YbodP  88  Y8 888888 dP  Yb 88  YbodP  88  Y8     88       88   88  ''')

print ('\n','---DATOS DE LOGIN---','\n')

usuario = input('Introduce tu usuario: ')
password = getpass.getpass()
ip = input('Introduce la IP del servidor: ')


def conectar ():
    try:
        ftp = FTP(ip)
        ftp.login(user=usuario, passwd=password)
        print ('Conexión exitosa')
        print (Fore.RED + 'Mostrando IP...' + Style.RESET_ALL)
        for i in tqdm(ip):
            print (i)
            time.sleep(0.5)
        
            
            
    except:
        print ('Conexión fallida')
        quit()
        
conectar()


        
print (Fore.MAGENTA, Back.BLUE + 'Hola, qué tal.')

    

        
    