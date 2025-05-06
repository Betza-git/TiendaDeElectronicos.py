import os
import time
  
#Seccion de funciones
def cls(): # Limpia la consola
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Linux/Mac
        os.system('clear')

def msg(msg):
    print(msg)

def pausa():
    if os.name == 'nt': # Windows
        os.system('pause')
    else: # Linux/Mac
        os.system('read -rsp "Presione Enter para continuar..."')

def pausaT(segundos):
    time.sleep(segundos)

def inicio(): 
    print("..................................")
    print("       \"Inicio de sesión\"       ")
    print("..................................")


def bienvenida():
    print("****************************************")
    print("*                                      *")
    print("*    ¡Bienvenidos a Eléctronica Py!    *")
    print("*                                      *")
    print("****************************************")  


def validarNumeroEntero(numero):
    try:
        return int(numero)
    except ValueError:
        msg("El valor ingresado no es un número entero...")
        return None
    
def validarNumeroFlotante(numero):
    try:
        return float(numero)
    except ValueError:
        msg("El valor ingresado no es un número decimal...")
        return None