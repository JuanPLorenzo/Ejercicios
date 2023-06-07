from config_juan import MAYORIA_EDAD
from config_juan import ALTURA_MINIMA
from config_juan import LETRA_PROHIBIDA



nombre ="Roberto"
edad = 30
altura = 180
peso = 90
japones = True
ruso = False

#Mayor de edad, medir mas de 150, hablar japones y/o ruso
#El nombre no puede contener la letra a

if(edad >= 18 and altura > 150 and (japones or ruso) and (not 'a' in nombre)):
    print("Contratado")
else:
    print("No cumple los requisitos")

#Solución con CONSTANTES



if(edad >= MAYORIA_EDAD and altura > ALTURA_MINIMA and (japones or ruso) and (not LETRA_PROHIBIDA in nombre)):
    print("Contratado")
else:
    print("No cumple los requisitos")