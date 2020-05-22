
# Librería para acceder a archivos CSV
import csv
# Librería para gestionar la entrada de los datos de la clase Contacto
import re
# Librería para manejar datos de tipo datetime
import datetime
# Módulo para poder ejecutar tareas directas en el sistema operativo.
import os
# Se importa una clase que permite extraer elementos de un objeto
from operator import attrgetter

from clasepia import Contacto

# Validador de expresiones regulares
# _txt es el texto a vlidar.
# _regex es el patrón de expresión regular a validar.
# Retorna True si _txt cumple con el patrón definido en _regex
# Retrona False si no es así.
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

# Se establece una función para borrar pantalla.
# Se usa, expresión lambda, que es equivalente a:
# def clear():
#   os.system('cls')
LimpiarPantalla = lambda: os.system('cls') #on Windows System

# Expresiones regulares para cada campo.
telefonoRegEx="^[0-9]{10}$"
nombreRegEx="^[A-Z]+(([',. -][A-Z ])?[A-Z]*)*$"

# Creando una lista vacía.
lista_contactos = []

# Lectura secuencial del archivo
with open('contactos_mobil.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    contador_lineas = 0
    
    # Lectura secuencial.
    for linea_datos in lector_csv:
        if contador_lineas == 0:
            # Si es la primer línea, muestro los nombres de campo y no guardo nada
            # en la lista.
            print(f'Los nombres de columna son {", ".join(linea_datos)}')
        else:
            # Si son datos (línea uno y posteriores)...
            # Genero una instancia de la clase Contacto, y le proporciono al constructor
            # los valores leidos del archivo.
            #objeto_temporal = Contacto({linea_datos[0]},{linea_datos[1]},{linea_datos[2]},{linea_datos[3]},{linea_datos[4]},{linea_datos[5]})
            objeto_temporal = Contacto(linea_datos[0],linea_datos[1],linea_datos[2],linea_datos[3],linea_datos[4],linea_datos[5])
            lista_contactos.append(objeto_temporal)

        # Se incrementa el número de líneas, pase lo que pase.
        contador_lineas += 1

    print(f'Procesadas {len(lista_contactos)} líneas.')

def mostrar_contactos(lista_contactos):
    # Ordenamiento.
    lista_contactos.sort(key=attrgetter("nickname"),reverse=False)

    print("Ordenado")
    # Barrido secuencial.
    for contacto in lista_contactos:
        print("------------------------------------------")
        print("Nick name: ", contacto.nickname)
        print("Nombre: ", contacto.nombre)
        print("Teléfono: ", contacto.telefono)
        print("Fecha nacimiento: ", contacto.fechanacimiento)
        print("Gastos: ", contacto.gasto)


def principal():
    while (True):
        LimpiarPantalla()
        print("LISTA DE COTACTOS")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            if opcion_elegida=="1":
                print("Llamar procedimiento para Agregar un contacto")
            if opcion_elegida=="2":
                print("Llamar procedimiento para Buscar un contacto")
            if opcion_elegida=="3":
                print("Llamar procedimiento para Eliminar un contacto.")
            if opcion_elegida=="4":
                print("Llamar procedimiento para Mostrar contactos.")
                mostrar_contactos(lista_contactos)
            if opcion_elegida=="5":
                print("Llamar procedimiento para Serializar datos.")

            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")



principal()