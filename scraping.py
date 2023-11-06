# -*- coding: utf-8 -*-
import requests, time, json
from datetime import date
from bs4 import BeautifulSoup
import diccionario

# os.system('cls')
url = 'https://supermercado.laanonimaonline.com/buscar?pag='
clave = '&clave='
path = "Precios.json"

def obtenerDatosJSON():
    # Obtiene los datos guardados en la base de datos, o bien, en caso de no tener, crea una nueva.
    try:
        with open(path, encoding="utf-8") as file:
            BdD = json.load(file)
    except:
        BdD ={}

    return BdD
#
def guardarDatosJSON(BdD):
  with open(path, "w", encoding="utf-8") as file:
    json.dump(BdD, file)
#
def BusquedaWeb(web):
    respuesta = requests.get(web)
    html = respuesta.text
    sopa =BeautifulSoup(html, 'html.parser')
    return sopa
#
def ObtenerPrecio(art):
  i=0
  conf = True
  while conf == True:
    i+=1
    web = url+str(i)+clave+diccionario.busqueda[art]
    sopa = BusquedaWeb(web)
    elemento= sopa.find_all('div', {"class" : "producto item text_center centrar_img fijar cuadro clearfix"})
        
    for el in elemento:
      dato = el.find("div",attrs={"class":"titulo02 aux1 titulo_puntos clearfix"}).a.text
      if dato == diccionario.articulo[art]:
        precio = el.find("div",attrs={"class":"precio semibold aux1"}).text
        
        conf = False
        break
  return precio
#
def CrearFilaPreciosHoy():
  PreciosArticulos = {}
  # Con este lazo obtengo los artículos a revisar
  for art in diccionario.articulo:
    print(art)
    PreciosArticulos[art] = ObtenerPrecio(art)
    # Se espera 0.1 segundos para no sobrecargar el servidor
    # print('#', sep=' ', end='', flush=True)
    time.sleep(0.1)
  return PreciosArticulos
#

ID = str(date.today())
PreciosBdD = obtenerDatosJSON()
if ID in PreciosBdD.keys():
  print(diccionario.mensajes['Ya realizado'])
else:
  PreciosArticulos = CrearFilaPreciosHoy()
  PreciosBdD[ID] = PreciosArticulos
  guardarDatosJSON(PreciosBdD)
  print(diccionario.mensajes['exito'])
