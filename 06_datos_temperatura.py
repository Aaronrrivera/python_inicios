num=int(input("Introduce un númro"))
if num<0:
    print("Muchísimo frio")
elif num>0 and num<=10:
    print("Fresquito")
elif num>10 and num<40:
    print("Calorcito")
else:
    print("Normalito")
    