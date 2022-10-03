import os
import re #para comprobar si lo que nos dan está bien
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
#comprobamos dni
def dni_valido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe cumplir el formato.")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI utilizado por otro cliente.")
            return False
    return True