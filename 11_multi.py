#Realizar un programa que solicite la introducción de un número y calcule su factorial 7! 
factorial=1
limite=int(input("introduce limite"))
for num in range(2,limite+1):
    factorial=factorial*num
print("Resultado factorial es {limite}:", factorial)