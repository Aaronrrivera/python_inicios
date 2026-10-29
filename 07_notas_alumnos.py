#lee la nota de un alumno, dependiendo del numero (0-10)
#Le indica si es suspenso (-5) aprobado (5 o 6)
#notable (7 o 8) o sobresaliente (9 o 10)

num1=int(input("Tú nota"))
match nota:
    case 0|1|2|3|4:
    print("Estás suspenso")
case 5|6:
    print("Estás aprobado")
case 7|8:
    print("Tienes un notable")
    case 9|10:
        print("Tienes un sobresaliente")
    case _:
        print("Nota no válida")