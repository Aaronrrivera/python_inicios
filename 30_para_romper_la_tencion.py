#pregunta al usuario que lenguaje quiere aprender. El programa le dirá si existe un curso para ese lenguaj o no

curso=["java","python","Typescryp","c","Dart"]
encontrado=False
lenguaje_programacion=input("Que lenguaje quieres aprender?")

"""
for c in curso:
    if c.lower==lenguaje_programacion.lower:
        print("lo tengo")
        encontrado=True
        break
if not encontrado:
    print("ni idea chacho")
"""
if lenguaje_programacion.lower() in [c.lower() for c in curso]:
    print("lo tengo")
else:
    print("ni idea chacho")
