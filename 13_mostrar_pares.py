#realiza un programa que solicite la introduccion de un numero despues, muesta todos los pares entre 1 y ese numero

num1=int(input("introduce numero"))
for num in range(1,num1+1):
    num1=num1/2
if n%2==0:
    print("solucion es par:", num1)