import os, requests, time
from bs4 import BeautifulSoup
import diccionario

import pickle

os.system('cls')

web = diccionario.busqueda['Yerba']
print(web)
def obtenerSopa(web):
    respuesta = requests.get(web)
    html = respuesta.text
    sopa =BeautifulSoup(html, 'html.parser')
    return sopa
#

sopa = obtenerSopa(web)

# Seccion copiar sopa a archivo y volver a traer como dato
# with open('SeguimientoInflacion/sopa.pickle', 'wb') as f:
#     pickle.dump(sopa, f)
# 
# with open('SeguimientoInflacion/sopa.pickle', 'rb') as f:
#     sopa = pickle.load(f)
# # 
# print(len(sopa))
# Fin de sección.

elemento= sopa.find_all('div', {"class" : "titulo02 aux1 titulo_puntos clearfix"})

for el in elemento:
    long = len(diccionario.articulo['Yerba'])
    articulo = el.find('a')['href']
    art = '/'+articulo[1:long]

    if art == diccionario.articulo['Yerba']:
        urlArt = diccionario.url + articulo    
        print(urlArt)
        sopaArt = obtenerSopa(urlArt)

        break


# Seccion copiar sopaArt a archivo y volver a traer como dato
# with open('SeguimientoInflacion/sopaArt.pickle', 'wb') as f:
#     pickle.dump(sopaArt, f)
# 
# with open('SeguimientoInflacion/sopaArt.pickle', 'rb') as f:
#     sopaArt = pickle.load(f)
# 
with open('SeguimientoInflacion/sopa_content.txt', 'w', encoding='utf-8') as file:
    file.write(str(sopaArt))
print(len(sopaArt))
# Fin de sección.

elemento= sopaArt.find_all('div', {"class" : "precio-promo"})
# <div class="precio destacado">$ 1.530<span class="decimales">,50</span></div>

print(len(elemento))
# for el in elemento:
#     print(el)
#     break