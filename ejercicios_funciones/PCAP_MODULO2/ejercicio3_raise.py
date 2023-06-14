#Suma número enteros pares
#Tenemos que asegurarnos que los parametros son número enteros pares
#Pasos:
#1- que sean enteros
#2- que sean pares

def sumar(s1 :int, s2:int):
    if not isinstance(s1,int) or not isinstance(s2,int):
        raise TypeError("Los parametros deben ser enteros")
    if s1%2 != 0 or s2%2 !=0:
        raise ValueError("Los parametos deben ser números pares")

    return s1+s2

try:
    sumar(4,8)
    sumar(4,9)
    sumar(4,8.8)
    sumar(4,True)
except(TypeError,ValueError) as error:
    print(error)


    '''
NO SON CONCRETAS:
BaseException
Exception
ArithmeticError
LookupError
ValueError

CONCRETAS:
FloatingPointError
ZeroDivisionError
IndexError
KeyError
TypeError'''