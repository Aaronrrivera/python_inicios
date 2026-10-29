contraseña=123
intentos=3
acertar=False
while intentos>0 and acertado==False:
    contraseña=input("Contraseña incorrecta, intentelo de nuevo:")
    if contraseña==password:
        acertar=True
    else:
        print("Contraseña válida")
        intentos=-1
if acertar==True:
    print("Válido")
else:
    print("No válido")
    
password="admin"
intentos=3
acertado=False
while intentos>0 and acertado==False:
    contra=input("Introduce contraseña ")
    if contra==password:
        acertado=True
    else:
        print("Vuelve a intentar!")
        intentos=intentos-1
if acertado==True:
    print("Usuario válido!")
else:
    print("Usuario no válido!") 