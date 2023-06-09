diccionario1 = {}
diccionario2 = dict()

diccionario = {1:'Uno',2:'Dos',3:'Tres', "Python": 1990}

print(diccionario[3])
print(diccionario.get('Python'))

#modificacion
diccionario[1]='One'
print(diccionario)

#eliminacion y obtencion
valor = diccionario.pop(1)
print(valor)

elemento = diccionario.popitem()
print(elemento)
print(diccionario)

pelicula1 =  {"titulo": "Titanic", "Sipnosis": "Barco se hunde", "Director": "Cameron", "Anio": "1998"}
pelicula2 = {"titulo":"Regreso al futuro","Sipnosis": "viajes en tiempo", "Director": "Zemeckis", "Anio": "1984"}