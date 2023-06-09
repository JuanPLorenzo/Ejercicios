tupla1 = ()
tupla2 = tuple() #tupla vacia
tupla3 = tuple([1,2,3])
tupla4 = (1,2,3)
tupla5 = (1) #Asigna un entero.
# las tuplas con un solo elemento se defines asi -> tupla6 = (1,)


print(type(tupla1))
print(type(tupla2))
print(type(tupla3))
print(type(tupla4))
print(type(tupla5))

#tuplas inmutables
#no se puede agregar elementos a la tupla
#no se puede eliminar a la tupla
#no se puede modificar a la tupla

tupla = ([1,2],[3,4],[5,6])
tupla[0]=[7,8] #¡ERROR¡
tupla[0][1]=8 # se puede modificar el contenido de los elementos de la tupla
print(tupla)
