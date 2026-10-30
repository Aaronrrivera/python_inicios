#al iniciar el programa se debe de mostrar el siguiente menú:
#1. Añadir nota
#2. Mostrar notas extremas
#3. Total de aprobados
#4. Nota media
#5 Mostrar todas
#6 Salir

#El usuario elige una opción del 1 al 6. El progrrma le pide los datos necesarios.
#Despues vuelve al menú hasta que elija la opción de salir

notas=[]
#funciones propias
def menu():
        print("1. añadir nota")
        print("2. mostrar notas extremas")
        print("3. total de aprobados")
        print("4. nota media")
        print("5. mostrar todas")
        print("6. salir")
def aprobados():
    aprobados=0
    for nota in notas:
        if nota>=5:
            aprobados+=1 
    return aprobados
def media():
suma=0
for nota in notas:
    suma+=nota
    if(len(notas)==0):
        return 0
    else:
        return suma/len(notas)

#programa principal
opcion_elegida=0
while opcion_elegida!=6:
    menu()
    opcion_elegida=int(input("elige una opcion"))
    
    match opcion_elegida:
        case 1:
            notas.append(int(input("introduce nota")))
        case 2:
            print(f"la nota mas alta es {max(notas)}")
        case 3:
            print(f"la nota mas baja es {min(notas)}")
        case 4:
            print(f"alumnos aprobados {aprobados()}")
        case 5:
                print(f"la nota media es {media()}")
        case 5:
            print(notas)
        case 6:
            print("fin")
        case _:
            print("no valido")    
        



