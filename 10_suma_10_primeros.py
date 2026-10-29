#Hacer un programa que muestre la suma de los 10 primeros numeros naturales
#Hacer un programa que muestre la suma de numeros entre el 1 y un numero leído por teclado


#suma=0
#for n in range(1,11):
#    suma=suma+n
#    print("Resultado: ", suma)
    
suma=0
limite=int(input("introduce límite"))
for n in range(1,limite+1):
    suma=suma+n
    print("Resultado: ", suma)
