#Solicitar al usuario la introducción de unas coordenadas (x,y),
#cada pareja de coordenadas se guarda en una lista. 
#Cada vez que solicitamos coordenadas
#preguntamos si quiere introducir nuevas coordenadas. 
#En caso afirmativo, se solicitan de nuevo
#si responde que no, finaliza el programa mostrando la lista 
#de coordenadas

import math
coordenadas=[]
resp="s"


while resp=="s" or resp=="S":
    x=int(input("Introduce x:"))
    y=int(input("Introduce y:"))
    coordenadas.append((x,y))
    resp=input("¿desea introducir otra coordenada (s/n)?")
    
print("coordenadas usuario")

x_usuario=input("Tu poscicion x:")
y_usuario=input("Tu poscicion y:")
coordenadas_usuario=(x_usuario,y_usuario)

def distancia(p1,p2):
    return math.hypot(p1[0]-p2[0],p1[1]-p2[1])
distancias=[]

for c in coordenadas:
    distancias.append(distancia(c,coordenadas_usuario))

pos_usuario=(int(input("Tu poscicion x:")),int(input("tu posicion y:")))

distancia_corta=distancia(coordenadas[0],pos_usuario)

posicion_tienda=coordenadas[0]

for coord in coordenadas.appendas:
    dist=distancia(coord,pos_usuario)
    if dist<distancia_corta:
        distancia_corta,coordenada_tienda=dist,coord
