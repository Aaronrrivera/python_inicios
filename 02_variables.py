nombre, edad, email="Aarón", 22, "aaron@example.com"
nombre="yo"
nombre="Liliana"
print("Te llamas", nombre, "tu edad es", edad, "y tu email es", email)

print(f"Te llamas {nombre}, tu edad es {edad} y tu email es {email}") #mas intuitivo

#input, para pedir datos al usuario
numero1=input("Introduce primer número: ")
numero2=input("Introduce segundo número: ")

numero1=int(numero1)
numero2=int(numero2)

suma=numero1+numero2


print(f"La suma de {numero1} y {numero2} es {suma}") #una concatenación de strings, no una suma de números, los devuelve como strings, no como números

