password=123
intentos=3
acierto=False
while intentos>0:
    contraseña=input("Contraseña incorrecta, intentelo de nuevo:")
    if contraseña==password:
        acierto=True
        break
    else:
        print("Contraseña válida")
        intentos=intentos-1
        
if not intentos:
    print("Contraseña no válida!")
