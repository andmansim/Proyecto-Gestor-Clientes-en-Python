import os
import platform #detecta el sistema operativo que queremos y lo adapta para poder trabajar con él.

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')
