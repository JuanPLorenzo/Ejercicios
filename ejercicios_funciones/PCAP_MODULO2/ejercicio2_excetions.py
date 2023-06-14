lista = [1,2, 3,4]

try:
    lista[10]
    print("ok")
except IndexError:
    print("KO")
except :
    print("No se")

