def saludar():
    print("hola")

def escribir_numero(numero):
    print(numero)

def dime_la_hora():
    return '17:41'

def calcular_el_doble(numero:int)-> int:
    return numero * 2

def sumar(a:int, b:int) -> int:
    return a+b

def escribir_numero_coloreado(numero, color):
    pass

print(sumar(1,2))

def escribir_texto_coloreado(texto, color='Rojo'):
    print(f"{texto} en color {color}")

#escribir_texto_coloreado()
escribir_texto_coloreado("Pelicula")
escribir_texto_coloreado("Pelicula","Verde")

def escribir_coloreado_formateado(texto, color='Rojo',formato ='negrita'):
    print(f"{texto},{color},{formato}")

escribir_coloreado_formateado("margarita")
escribir_coloreado_formateado("margarita","Verde")
escribir_coloreado_formateado("margarita", color ='Verde')
escribir_coloreado_formateado("margarita",color ='Verde',formato='cursiva')
escribir_coloreado_formateado("margarita",formato ='cursica', color ='Verde')
escribir_coloreado_formateado("margarita",formato ='cursiva'),


def calcular_eldoble_y_eltriple(numero):
    doble = numero *2
    triple = numero * 3
    return doble, triple

