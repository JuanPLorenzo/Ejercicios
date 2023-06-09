diccionario = {}#Genera diccionario vacio
conjunto = {1,2,3} #set de 3 elementos
conjunto = set()
conjunto = set([1,2,3])
conjunto = set((1,2,3))

frutas_invierno ={'Naranja','Limón','Uva', 'Limón'}
print(frutas_invierno)

frutas_verano ={'Sandía','Melón','Ciruela','Naranja'}
print(frutas_verano)

print(frutas_invierno.isdisjoint(frutas_verano))

print(frutas_invierno.intersection(frutas_verano))

print(frutas_invierno.difference(frutas_verano))


#Alexa
base_conocimiento = [
    ("Tienes dime hora".lower(),"Son las 18:52"),
    ("Dime como se hace la tortilla de patatas".lower(),"Pela patatas,pica cebolla...."),
    ("Qué tiempo hace".lower(),"Esta lloviento"),
    ("Cual es la capital de alemania".lower(),"Berlín"),
]


pregunta = input("Que quieres saber?: ")

elementos_pregunta = set(pregunta.lower().split())
print(elementos_pregunta)

intersecciones = 0
for conocimiento in base_conocimiento:
    elementos_conocimiento = set(conocimiento[0].split())
    intersecciones_actuales = len(elementos_pregunta.intersection(elementos_conocimiento))
    if intersecciones_actuales > intersecciones:
        mejor_respuesta = conocimiento[1]
        intersecciones = intersecciones_actuales

if intersecciones > 0:
    print(mejor_respuesta)
else:
    print("No entiendo la pregunta")



