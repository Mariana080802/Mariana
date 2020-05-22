import csv

import datetime

class Contacto:
  def _init_(self, nickname, nombre, correo, telefono, gasto,fechanacimiento=datetime.datetime.now(),UIValido=False):
    self.nickname=nickname
    self.nombre=nombre
    self.correo=correo
    self.telefono=telefono
    self.gasto=gasto
    self.UIValido=UIValido

with open('contactos_mobil.csv', newline='') as archivo_csv:

    lector_csv = csv.reader(archivo_csv, delimiter='|')

    for e in lector_csv:

      Contacto.append(Contacto(e[0],e[1],e[2],e[3],e[4],e[5]))