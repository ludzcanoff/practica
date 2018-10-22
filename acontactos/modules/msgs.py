#!usr/bin/python
# -*-coding: utf-8 -*-
from compat import clr

def intro():
    print('''\n╔══════════════════════════╗\n║ADMINISTRADOR DE CONTACTOS║
╚══════════════════════════╝''')

def error():
    clr()
    print('''\n╔══════════════════════════════════════╗
║¡La opción seleccionada es incorrecta!║
╚══════════════════════════════════════╝''')
    slp()
    clr()
