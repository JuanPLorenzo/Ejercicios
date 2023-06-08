'''for i in range(0,10,2):
    print(i)



tupla = ("Fernando","Francisco","Alberte")
for nombre in tupla:
    print (nombre.upper())'''


tupla = ("Fernando","Francisco","Alberte")
for nombre in tupla:
    print (nombre.upper())
    if 'i' in nombre:     
        break
else:
    print('Fin')