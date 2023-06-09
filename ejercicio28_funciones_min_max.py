#max y min

lista = [3,8, -4,5]
print(max(lista))

ciudades = [('Pontevedra',10),('A Coruña',8),('Vigo', 7), ('Orense',10)]

def valorar(ciudad):
    valoracion = ciudad[1]
    return valoracion

print(max(ciudades, key = valorar))
print(min(ciudades, key = valorar))