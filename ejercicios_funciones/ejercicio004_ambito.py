def funcion1():
    x =5
    print(x)

x = 8
funcion1()
print(x)

def funcion2(x):
    x=x+1
    print(x)

x=8
funcion2(x)
print(x)

def funcion3():
    '''
    x = x+1#da error por que aquí intenta acceder a una variable x local en el incremento
    print(x)'''

    global x #Quiero que utilices la x global y no creas una nueva variable local
    # para utilizar global dentro de una función hay que tener muy buenas razones
    # si no mejor evitarlo. El uso de variables globales hay que evitarlo en general
    x=x+1
    print(x)

x=8
funcion3()
print(x)


'''
def sumar():
    print("suma 1")

def sumar():
    print("sumar 2")

sumar()'''


