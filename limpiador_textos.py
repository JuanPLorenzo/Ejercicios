def limpiar_texto(texto, str_letras_a_eliminar, caracter_susitucion):
    for letra in str_letras_a_eliminar:
        texto = texto.replace(letra, caracter_susitucion)
    return texto



cadena0 = 'aeiou'
cadena1 = "ai"
caracter_sust ="-"
nueva_cadena = limpiar_texto(cadena0,cadena1,caracter_sust)
print(nueva_cadena)
