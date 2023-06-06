'''frase = "Me gusta ver atardecer desde el balcón"
texto_a_buscar = input("Introduce el texto a buscar: ")

#El texto 'ver' aparece 1 veces
frase_may = frase.upper()
numero_veces_min = frase.count(texto_a_buscar)
numero_veces_may = frase_may.count(texto_a_buscar.upper())
print(numero_veces_min)
print(numero_veces_may)

num_veces = frase.upper().count(texto_a_buscar.upper())
print(num_veces)

print(f'El texto \'{texto_a_buscar}\' es {num_veces}')

frase = "Me gusta ver atardecer desde el balcón"

print(frase[0:10].upper().capitalize()[3:].replace('a', '@'))'''


palabras_prohibidas = "momia vampiro ajo clavo estaca"
palabra = input("Introduce una palabra:")
#Indicar si la palabra introducida está o no prohibida (sin importar si es mayúsculas o minúsculas)

if palabra.upper() in palabras_prohibidas.upper():
    print(f"La palabra {palabra} esta prohibida")
else:
    print(f"La palabra {palabra} es correcta")
