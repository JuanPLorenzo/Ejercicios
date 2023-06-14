def cuantificador(elemento):
    return elemento[1]


lista1 =[3,8,0,15,1]
lista1.sort()
print(lista1)


lista2= sorted(lista1)
print(lista1)
print(lista2)

cartera = [('bbva',1000),('acs', 5000),("telefonica",300)]
cartera.sort(key=cuantificador)
print(cartera)

cartera.sort(key=cuantificador, reverse=True)
print(cartera)

print('----------')

for elemento in cartera:
    print(elemento)
    print(cartera)

