#!usr/bin/python
# -*-coding: utf-8 -*-
import os
from mc import *
from contact import *

os.system('chcp 65001>nul')


def ppal():

    seleccion = ''
    while seleccion != 0:
        clr()
        intro()
        print('''\n╔══════════════════════════════════════════════════════════════════════════════╗
║                                Menú Principal                                ║
╚══════════════════════════════════════════════════════════════════════════════╝''')
        print('''\n(1) Para añadir contacto(s) a un archivo CSV.
        \n(2) Para visualizar sus contactos en un archivo CSV.
        \n(3) Para añadir contacto(s) a un archivo sin extensión.
        \n(4) Para visualizar sus contactos en un archivo sin extensión.''')
        seleccion = raw_input('\n\nIndique la opción deseada, o (0) para salir:')

        if seleccion == '1':
            clr()
            editarcsv()
        elif seleccion == '2':
            clr()
            visualizarcsv()
            salir()
        elif seleccion == '3':
            clr()
            editar()
        elif seleccion == '4':
            clr()
            visualizar()
            salir()
        elif seleccion == '0':
            clr()
            thank()
            exit()
        else:
            error()
#Joaquín Ludzcanoff, 2018