resp="s"
while resp=="s" or resp=="S":
    num=int(input("Introduce un mumero"))
    if num%2==0:
        print("par")
    else:
        print("impar")
    resp=input("¿desea introducir otro numero (s/n)?")


