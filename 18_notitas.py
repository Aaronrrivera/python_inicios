#Solicita una nota, despues otra, y asi sucesivamente hasta introducir un cero 
# y no podrá pedir mas notas y mostrara la media 
suma=0
total=0
nota=int(input("Introduce nota"))
while nota>0:
    total=total+1
    suma=suma+nota
    nota=int(input("introduce nota"))
try:
    print(f"Has introducido {total} notas, y la media es: {su/total}")
except ZeroDivisionError:
    print("media 0")