from definirclase import Contacto

import os

import re
from operator import attrgetter

LimpiarPantalla = lambda: os.system('cls') 
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

def principal():
    while (True):
        LimpiarPantalla()
        print("LISTA DE CONTACTOS")
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
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="2":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="4":
                print("Llamar procedimiento para la acción")
                Contacto.sort(key=attrgetter("telefono"),reverse=False)
                print("Ordenado")
                for contacto in Contacto:
                 print("------------------------------------------")
                 print(contacto.nickname)
                 print(contacto.nombre)
                 print(contacto.correo)
                 print(contacto.telefono)
                 print(contacto.gasto)
                 print(contacto.UIValido)
            if opcion_elegida=="5":
                print("Llamar procedimiento para la acción")

            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")

principal()