#sabe japones; movilidad; 24x7; python

fina=('fina',False, True, False,0.4)
fernando =('fernando',True, False, True, 0.6)
daniel_sama = ('daniel',True, True, True, 0.5)

candidatos =(fina, fernando, daniel_sama)

for candidato in candidatos:
    print(f"Evaluando japonés de {candidato[0]}")
    if candidato[1] == False:
        continue #cuando un candidato no se cumple, pasa al siguiente alemento de la tupla
    print(f"Evaluando movilidad de {candidato[0]}")
    if candidato[2] == False:
        continue
    print(f"Evaluando 24x7 de {candidato[0]}")
    if candidato[3] == False:
        continue
    print(f"Evaluando python de {candidato[0]}")
    if candidato[4] <0.5:
        continue
    print(f"Candidato {candidato[0]} aceptado")
    
    
