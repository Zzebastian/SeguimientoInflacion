#  Nota: Importante instalar el paquete "schedule"
import os, requests, time
from bs4 import BeautifulSoup
import diccionario
os.system('cls')
url = 'https://supermercado.laanonimaonline.com/buscar?pag='
clave = '&clave='

i=1

web = url+str(i)+clave+diccionario.busqueda['Yerba']
print(web)
# def BusquedaWeb(web):
# respuesta = requests.get(web)
# html = respuesta.text
# sopa =BeautifulSoup(html, 'html.parser')

# Seccion copiar sopa a archivo y volver a traer como dato
import pickle
# with open('SeguimientoInflacion/sopa.pickle', 'wb') as f:
#     pickle.dump(sopa, f)
# 
with open('SeguimientoInflacion/sopa.pickle', 'rb') as f:
    sopa = pickle.load(f)
print(len(sopa))
# Fin de sección.

elemento= sopa.find_all('div', {"class" : "producto item text_center centrar_img fijar cuadro clearfix"})
print(len(elemento))
for el in elemento:
  dato = el.find("div",attrs={"class":"titulo02 aux1 titulo_puntos clearfix"}).a.text
  if dato == diccionario.articulo['Yerba']:
    precio = el.find("div",attrs={"class":"precio semibold aux1"}).text
    break





# def ObtenerPrecios(descanso):
# #   El descanso se utiliza
#   for producto in diccionario.articulo:
#     print(diccionario.articulo[producto])
#     precio = BusquedaWeb(diccionario.articulo[producto])
#     print(precio)
#     time.sleep(descanso)
# #

# ObtenerPrecios(2)