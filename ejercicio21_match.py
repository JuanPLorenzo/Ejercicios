#0; ok,1:En marcha, 2:Parado, 3:Averiado

estado = 3

match estado:
    case 0:
        print('ok')
    case 1:
        print('En marcha')
    case 2:
        print('parado')
    case 3:
        print('Averiado')
    case _:
        print("Desconocido")

nombre = input("Introduce un nombre: ")

match nombre.lower():
    case 'fernando':
        print('46')
    case 'juan':
        print('58')
    case 'tamara':
        print('25')
    case 'amalia':
        print('35')
    case _:
        print("Desconocido")


