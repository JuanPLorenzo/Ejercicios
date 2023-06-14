'''
clase vs (objeto o instanacia)
'''

class Tractor:
    #constructor: Siempre recibe self como primer argumento;
    def __init__(self, _nombre, _color, _marca):  
        self.nombre =_nombre
        self.color= _color
        self.marca =_marca
        self.combustible = 0
        self.posicion =[5,5]

    def arrancar(self):
        print(f"{self.nombre} arrancando ......")

    def desplazar(self, delta_x, delta_y):
        if self.combustible>0:
            print(f"soy {self.nombre} y esta es mi posición actual: {self.posicion}")
            self.posicion = [self.posicion[0]+delta_x,self.posicion[1]+delta_y]
            print(f"soy {self.nombre} y esta es mi posición después de desplazarme: {self.posicion}")
        else:
            print("No tengo combustible")
    
    def repostar(self,litros):
        print(f"soy {self.nombre} y estoy repostando {litros} litros agrícolas")
        self.combustible += litros
        





lista = list()
tractor1 = Tractor('manolito','rojo','john deere')

tractor1.arrancar()
tractor1.desplazar(1,1)
print(tractor1.combustible)
tractor1.repostar(3)
tractor1.desplazar(1,1)





    

