#  Nota: Importante instalar el paquete "schedule"
import os, requests, time, json
from bs4 import BeautifulSoup
import diccionario
os.system('cls')
url = 'https://supermercado.laanonimaonline.com/buscar?pag='
clave = '&clave='
PreciosArticulos = {}

# def obtenerDatosJSON():
#     # Obtiene los datos guardados en la base de datos, o bien, en caso de no tener, crea una nueva.
#     try:
#         with open("Precios.json") as file:
#             BdD = json.load(file)
#     except:
#         BdD ={}

#     return BdD
# #
# def guardarDatosJSON(BdD):
#   with open("Precios.json", "w") as file:
#     json.dump(BdD, file)
# #
# def agregarDatos():
#    ID = 10 # Fecha en AA-MM-DD ############

#
def BusquedaWeb(web):
    respuesta = requests.get(web)
    html = respuesta.text
    sopa =BeautifulSoup(html, 'html.parser')
    return sopa
#

# preciosBdD = obtenerDatosJSON()


for art in diccionario.articulo:
  i=0
  conf = True
  while conf == True:
    i+=1
    web = url+str(i)+clave+diccionario.busqueda[art]
    print(web) #
    sopa = BusquedaWeb(web)
    elemento= sopa.find_all('div', {"class" : "producto item text_center centrar_img fijar cuadro clearfix"})
        
    for el in elemento:
      dato = el.find("div",attrs={"class":"titulo02 aux1 titulo_puntos clearfix"}).a.text
      if dato == diccionario.articulo[art]:
        precio = el.find("div",attrs={"class":"precio semibold aux1"}).text
        PreciosArticulos[art] = precio
        conf = False
        break
  # Se espera 1 segundo para no sobrecargar el servidor
  time.sleep(1)
  # 

print(PreciosArticulos)
for el in PreciosArticulos:
  print(el)
  print(PreciosArticulos[el])
  print('')