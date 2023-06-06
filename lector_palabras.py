def get_lines_from_file(file_name):
    fichero = open(file_name, mode="r", encoding="utf-8")
    lineas = fichero.readlines()
    lineas = [linea.replace('\n','') for linea in lineas]
    fichero.close()
    return lineas

if __name__ == '__main__':
    lineas = get_lines_from_file("F:\PYCNTG\Ejercicios\palabras_prohibidas.txt")
    print(lineas)