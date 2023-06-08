import random
numero_secreto = random.randint(1,6)
'''
acierto = False
while not acierto:
    numero = int(input ('introduce un número entre 1 y 6 : '))
    print(numero)
    if numero == numero_secreto:
        acierto = True  
        print('Acierto')    
    else:
        acierto = False
        print('Repite')
else:
    print('Fin.')'''

num_intentos = 0
acierto = False
while not acierto and num_intentos <3 :
    numero = int(input ('introduce un número entre 1 y 6 : '))
    print(numero)
    if numero == numero_secreto:
        acierto = True  
        print('Acierto')    
    else:
        acierto = False
        if num_intentos == 2:
            print('Has llegado al número máximo de intentos')
        else:
            print('Repite.')
    num_intentos +=1
    
else:
    print('Fin.')