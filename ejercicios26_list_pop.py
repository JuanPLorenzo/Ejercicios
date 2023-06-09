#x = print
#x("Juan")

'''
ciudades = [('Pontevedra',10),('A Coruña',8),('Vigo', 7), ('Orense',10)]

def valorar(ciudad):
    valoracion = ciudad[1]
    return valoracion

#ciudades.sort(key = valorar)
ciudades.sort(key = valorar, reverse= True)
print(ciudades)
print(f"La mejor ciudad para pasear es {ciudades[0][0]}")'''



#Representar una estructura de datos que contenga:
#Nombre de un restaurante
#Valoracion de la calidad (0,10)
#Valoración del precio (0,10)
#Valoración de la ubicación (0,10)

#calidad * 3 + Precio*2 + ubicación * 1

restaurante1 = ("Burguer King", 7, 10, 0)
restaurante2 = ("Artabra", 10, 8, 8)
restaurante3 = ("Acibro", 9, 9, 6)

restaurantes = [restaurante1, restaurante2, restaurante3]

def calificar_restaurante(restaurante):
    valoracion = restaurante[1]*3 + restaurante[2]*2 + restaurante[3]
    return valoracion

restaurantes.sort(key = calificar_restaurante, reverse = True)
print(f"El restaurante cadidato es {restaurantes[0][0]}")

restaurante1 = ("Burguer King", 7, 10, 0)
restaurante2 = ("Artabra", 10, 8, 8)
restaurante3 = ("Acibro", 9, 9, 6)


restaurantes = [restaurante1, restaurante2, restaurante3]

restaurantes_ordenados=sorted(restaurantes, key = calificar_restaurante, reverse = True)
print(restaurantes)
print(restaurantes_ordenados)












