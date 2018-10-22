#!usr/bin/python
# -*-coding: utf-8 -*-

import os


def winutf8():
    os.system('chcp 65001 >nul')


def clr():
    if os.name == 'posix':
        os.system('clear')
    if os.name == 'nt':
        os.system('cls')


def slp():
    if os.name == 'posix':
        os.system('sleep 6')
    if os.name == 'nt':
        os.system('timeout 6 >nul')


def intro():
    print('''\n╔══════════════════════════╗                          ┌────────────────────────┐
║ADMINISTRADOR DE CONTACTOS║                          │Joaquín Ludzcanoff, 2018│
╚══════════════════════════╝                          └────────────────────────┘''')


def firstrun():
    existe = os.path.isfile('contactos')
    if existe is True:
        clr()
        intro()
        slp()
    if existe is False:
        clr()
        intro()
        print('''\n╔══════════════════════════════════════════════════════════════════════════════╗
║                     ¡ARCHIVO DE CONTACTOS NO ENCONTRADO!                     ║
║              No podrá visualizar archivos hasta que genere uno               ║
║          El archivo se generará automáticamente al añadir contactos.         ║
╚══════════════════════════════════════════════════════════════════════════════╝''')
    existecsv = os.path.isfile('contactos.csv')
    if existecsv is True:
        slp()
    if existecsv is False:
        print('''\n╔══════════════════════════════════════════════════════════════════════════════╗
║                   ¡ARCHIVO DE CONTACTOS CSV NO ENCONTRADO!                   ║
║              No podrá visualizar archivos hasta que genere uno               ║
║El archivo se generará automáticamente al añadir contactos a un archivo *.csv.║
╚══════════════════════════════════════════════════════════════════════════════╝''')
        slp()


def error():
    clr()
    print('''\n╔══════════════════════════════════════════════════════════════════════════════╗
║                    ¡La opción seleccionada es incorrecta!                    ║
╚══════════════════════════════════════════════════════════════════════════════╝''')
    slp()
    clr()


def salir():
    salir = raw_input('Indique (0) para volver al menú principal: ')
    if salir == '0':
        if os.name == 'posix':
            os.system('sleep 0')
        if os.name == 'nt':
            os.system('timeout 0 >nul')
    else:
        error()


def thank():
    print('''\n╔══════════════════════════════════════════════════════════════════════════════╗
║                        ¡Gracias por usar el programa!                        ║
╚══════════════════════════════════════════════════════════════════════════════╝''')
    slp()
    clr()
#Joaquín Ludzcanoff, 2018