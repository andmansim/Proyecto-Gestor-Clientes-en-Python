import os
import platform #detecta el sistema operativo que queremos y lo adapta para poder trabajar con él.

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

#Es para poder leer un texto cómodamente
def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto