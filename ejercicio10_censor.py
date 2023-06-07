import lector_palabras

lineas = lector_palabras.get_lines_from_file("F:\PYCNTG\Ejercicios\palabras_prohibidas.txt")
print(lineas)


diccionario = {"mameluco":"Hombre necio y bobo","gaznápiro":"Palurdo, simplón, torpe, que se queda embobado con cualquier cosa"}
for clave in diccionario.keys():
    print(clave)
for valor in diccionario.values():
    print(valor)
for clave, valor in diccionario.items():
    print(clave, valor)