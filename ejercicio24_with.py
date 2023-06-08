#lectura de un fichero sin with

fichero_palabras = open("palabras_prohibidas.txt", mode='r',encoding="utf-8")
datos = fichero_palabras.read(10)
print(datos)
fichero_palabras.close()

