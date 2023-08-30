#  Nota: Importante instalar el paquete "schedule"


import os, requests, time
from bs4 import BeautifulSoup
import diccionario
os.system('cls')

# web = diccionario.articulo['Yerba']
def BusquedaWeb(web):
  
  respuesta = requests.get(web)
  html = respuesta.text
  sopa =BeautifulSoup(html, 'html.parser')
  
  # print(len(sopa))
  
  elemento= sopa.find_all('div', {"class" : "precio destacado"})
  # print(len(elemento))
  # <div class="precio destacado">$ 1.378<span class="decimales">,70</span></div>
  el = str(elemento)
  
  # Parte entera
  N1 = el.find('do">$ ')
  N2 = el.find('<span ')
  ent = el[N1+6 : N2].replace('.','')
  
  # Parte decimal
  n1 = el.find('es">')
  dec = el[n1+4 : n1+7].replace(',','.')
  
  Num = ent+dec
  Precio = float(Num)
  
  return Precio
#

# def ObtenerPrecios(descanso):
# #   El descanso se utiliza
#   for producto in diccionario.articulo:
#     print(diccionario.articulo[producto])
#     precio = BusquedaWeb(diccionario.articulo[producto])
#     print(precio)
#     time.sleep(descanso)
# #

# ObtenerPrecios(2)