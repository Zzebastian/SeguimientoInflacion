import requests # https://docs.python-requests.org/en/v2.0.0/
from bs4 import BeautifulSoup as bs # https://tedboy.github.io/bs4_doc/
i = 0
query= input("Inserte query: ")
while True:
  i = i+1
  url_base= "https://supermercado.laanonimaonline.com/buscar?pag="+str(i)+"&clave="
  print(url_base+query)
  page=bs(requests.get(url_base+query).text, "html.parser")
  array= page.find_all("div",attrs={"class":"producto item text_center centrar_img fijar cuadro clearfix"})
  if len(array)<1:
    print(len(array))
    break
  for x in array:
    print(x.find("div",attrs={"class":"titulo02 aux1 titulo_puntos clearfix"}).a.text)
    print(x.find("div",attrs={"class":"precio semibold aux1"}).text)


# import os, requests, time
# from bs4 import BeautifulSoup

# url = 'https://supermercado.laanonimaonline.com/buscar?pag=1&clave='
# query = 'Yerba'
# web = url+query
# print(web)
# def obtenerSopa(web):
#     respuesta = requests.get(web)
#     html = respuesta.text
#     sopa =BeautifulSoup(html, 'html.parser')
#     return sopa
# #

# sopa = obtenerSopa(web)


# # Seccion copiar sopa a archivo y volver a traer como dato
# import pickle
# with open('SeguimientoInflacion/sopa2.pickle', 'wb') as f:
#     pickle.dump(sopa, f)

# # with open('SeguimientoInflacion/sopa.pickle', 'rb') as f:
# #     sopa = pickle.load(f)
# # # 
# print(len(sopa))
# # Fin de sección.

# array = sopa.find_all('div', attrs={'class':'producto item text_center centrar_img fijar cuadro cleafix'})
# for x in array:
#     print(x.find('div', attrs={'class': 'titulo02 aux1 titulo_puntos clearfix'}).a.text)
#     print(x.find('div', attrs={'class': 'precio semibold aux1'}).text)