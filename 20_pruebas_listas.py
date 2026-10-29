#Listas: 

lista=[4,1,8,2,11]

#muestra cada numeros pares de la lista
for num in lista:
    if num%2==0:
        print(num)
        
#sustirulle cada elemento de la lista por su cuadrado
#imprimir la lista entera y la suma de todo su contenido

"""
indice=0
for num in lista:
    lista[indice]=num*num
    indice=indice+1
print(lista)
suma=0
for num in lista:
    suma=suma+num
print(f"la sua de los datos de la lista {lista} es {suma}")
"""
#solucion alternativa

for indice, num in enumerate (lista):
    lista[indice]=num**2
print(lista)
suma=0
for num in lista:
    suma=suma+num
print(f"la sua de los datos de la lista {lista} es {suma}")

