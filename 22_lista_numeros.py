#Solicita la introduccion de numeros
#uno a nuo, guarda los resultados en una lista despues de pedirlos.
#pregunta si quiere introducir otro, hasta que diga que no. luego mostrar lista

resp="s"
lista=[]

while resp=="S" or resp=="S":
   try:
        num=int(input("Introduce un número"))
        lista.append(num)
        resp=input("¿añadir otro más?")
   except ValueError:
        print("No valor númerico")
       
print(f"la lista es: {lista}")


