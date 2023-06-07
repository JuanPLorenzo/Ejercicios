#Ejecutar previamente: pip install gTTS
from gtts import gTTS
import os
  
#mytext = 'Voy a invadir la Tierra y voy a utilizar a los humanos como mano de obra barata'
language = 'es'
pregunta_nombre = '¿Cual es tu nombre?'
myobj1 = gTTS(text=pregunta_nombre, lang=language, slow=False)
myobj1.save("locucion_nombre.mp3")
os.system("start locucion_nombre.mp3")
nombre = input('Nombre: ')

pregunta_genero = '¿Eres Hombre o Mujer ?'
myobj2 = gTTS(text=pregunta_genero, lang=language, slow=False)
myobj2.save("locucion_genero.mp3")
os.system("start locucion_genero.mp3")

genero = input('Genero (H/M): ')
if genero.upper() == 'H':
    tratamiento = 'amo y señor'
else:
    tratamiento = 'ama y señora'

mytext = f'Hola {nombre}, eres mi {tratamiento} y te obedeceré en todo lo que quieras'

myobj3 = gTTS(text=mytext, lang=language, slow=False)
myobj3.save("locucion.mp3")
os.system("start locucion.mp3")



#os.system("start locucion.mp3")#No funciona en Linux
#Preguntar al usuario su nombre.
#Preguntar al usuario si es H/M/?
#Hola Fernando, eres mi amo y señor y te obedeceré en todo lo que quieras
#Hola Vanessa, eres mi ama y señora y te obedeceré en todo lo que quieras