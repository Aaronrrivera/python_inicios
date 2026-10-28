#Teniendo en cuenta que alevín es 10 y Benjamin es 16. Hacer un programa que solicite a edad y nos muestre a que grupo pertenece
#El más cercano a tu edad, esta debe de estar entre 9 y 18 años

Inf,Sup,Benjamin,Alevin=9,18,16,10
edad=int(input("Tú edad"))
if edad<Inf or edad>Sup:
     print("Edad no válida")
else:
    distancia_benjamin=edad-Benjamin
    distancia_alevin=Alevin-edad
    if distancia_benjamin<distancia_alevin:
        print("Eres Benjamin")
    else:
        print("Eres Alevin")