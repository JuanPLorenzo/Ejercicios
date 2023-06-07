def evaluar(valor, numero):
    print("Evaluado", numero)
    return valor

if evaluar(True, 1) and evaluar(False,2):
    print("OK")
else:
    print("KO")