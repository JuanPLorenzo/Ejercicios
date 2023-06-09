#pip install requests
import requests
import json

KEY ='98c7f479'
URL ='http://www.omdbapi.com/'
#https://www.omdbapi.com/?t=Star%20Wars&apikey=98c7f479
titulo = input("Titulo de la pelicula: ")

parametros = {'apikey':KEY,'t': titulo}
r = requests.get(URL, params = parametros)
if r.status_code == 200:
    pelicula_dict = r.json()

else: print("Ha ocurrido un error HTTP")


#Mostrar Titulo, Director, sipnosis, Año de estreno y actores
print(pelicula_dict.get("Title", "No dispongo de Titulo"))
print(pelicula_dict.get("Director", "No dispongo de Director"))
print(pelicula_dict.get("Plot", "No dispongo de Sipnosis"))
print(pelicula_dict.get("Year", "No dispongo de de Año"))
print(pelicula_dict.get("Actors", "No dispongo de Actores"))






