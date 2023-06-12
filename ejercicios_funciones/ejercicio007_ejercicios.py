def saludar():
    pass

#Función que calcule la suma de dos números

def sumar(a, b):
    return a + b
#Función que calcule la suma de un número indeterminado de números

def sumar1 (*values):
    suma = 0
    for val in values:
        suma += val
    return suma

print(sumar1(1,2,3))

#Función que escriba en un fichero un texto
def escribir_fichero(nombre_fichero, texto):
    f= open(nombre_fichero,mode='w',encoding='utf-8')
    f.write(texto)
    f.close()




#Función que traduzca un texto a un idioma
def traducir(texto, idioma_origen, idioma_destino):
    pass
#Función que calcule el número de primitiva de la próxima semana
#Función que proporciona el pronóstico del tiempo de una semana determinada en un lugar concreto