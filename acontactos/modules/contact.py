#!usr/bin/python
# -*-coding: utf-8 -*-

import csv
from mc import *


def loop1():
    otro = raw_input('\n(1) para añadir otro contacto, o (0) para volver al menú principal: ')
    if otro == '0':
        if os.name == 'posix':
            os.system('sleep 0')
        if os.name == 'nt':
            os.system('timeout 0 >nul')
    elif otro == '1':
        existecsv = os.path.isfile('contactos.csv')
        if existecsv is True:
            editarcsv()
        else:
            print('No deberías haber podido llegar aquí. Felicitaciones!')
    else:
        error()
        loop1()


def loop2():
    otro = raw_input('\n(1) para añadir otro contacto, o (0) para volver al menú principal: ')
    if otro == '0':
        if os.name == 'posix':
            os.system('sleep 0')
        if os.name == 'nt':
            os.system('timeout 0 >nul')
    elif otro == '1':
        existe = os.path.isfile('contactos')
        if existe is True:
            editar()
        else:
            print('No deberías haber podido llegar aquí. Felicitaciones!')
    else:
        error()
        loop2()


def editarcsv():
    print('''\n╔═══════════════════════════════════╗
║Agende contactos a un archivo *.csv║
╚═══════════════════════════════════╝''')
    nombre = raw_input('Ingrese su nombre: ')
    apellido = raw_input('\nIngrese su apellido: ')
    telefono = raw_input('\nIngrese su número telefónico: ')
    email = raw_input('\nIngrese su dirección de correo electrónico: ')
    archivo = csv.writer(open('contactos.csv', 'ab'))
    archivo.writerow([nombre, apellido, telefono, email])
    loop1()


def visualizarcsv():
    existe = os.path.isfile('contactos.csv')
    if existe is True:
        print('''\n╔═══════════════════════════════════════╗
║Visualize contactos en un archivo *.csv║
╚═══════════════════════════════════════╝''')
        archivo = open('contactos.csv', 'r')
        for line in archivo:
            linea = line.split(',')
            nombre = linea[0]
            apellido = linea[1]
            telefono = linea[2]
            email = linea[3]
            print '\n',
            print 'Nombre:', nombre, '| Apellido:', apellido
            print 'Número telefónico:', telefono, '|Casilla de correo:', email
        archivo.close()
    elif existe is False:
        print('''\n╔═══════════════════════════════════╗
║¡El archivo de contactos no existe!║
╚═══════════════════════════════════╝''')
        slp()


def editar():
    print('''\n╔═══════════════════════════════════════════╗
║Agende contactos a un archivo sin extensión║
╚═══════════════════════════════════════════╝''')
    nombre = raw_input('Ingrese su nombre: ')
    apellido = raw_input('\nIngrese su apellido: ')
    telefono = raw_input('\nIngrese su número telefónico: ')
    email = raw_input('\nIngrese su dirección de correo electrónico: ')
    archivo = csv.writer(open('contactos', 'ab'))
    archivo.writerow([nombre, apellido, telefono, email])
    loop2()


def visualizar():
    existe = os.path.isfile('contactos')
    if existe is True:
        print('''\n╔═══════════════════════════════════════════════╗
║Visualize contactos en un archivo sin extensión║
╚═══════════════════════════════════════════════╝''')
        archivo = open('contactos', 'r')
        for line in archivo:
            linea = line.split(',')
            nombre = linea[0]
            apellido = linea[1]
            telefono = linea[2]
            email = linea[3]
            print '\n',
            print 'Nombre:', nombre, '| Apellido:', apellido
            print 'Número telefónico:', telefono, '|Casilla de correo:', email
        archivo.close()
    elif existe is False:
        print('''\n╔═══════════════════════════════════╗
║¡El archivo de contactos no existe!║
╚═══════════════════════════════════╝''')
#Joaquín Ludzcanoff, 2018