#dada esa lista de notas, crea otra lista que contenga solo los aprobados.
#ademas le añadiras un punto extra a cada uno
#finalmente se imprime la lista

numeros=[4,3,7,9,2]
"""
aprobados=[]
for nota in numeros:
    if nota>=5:
        aprobados.append(nota+1)
""" 
#compresion de listas
#funcion que haga la tarea indicada arriba.
#Resultado en tupla
def obtener_aprobados():
    return tuple([nota+1 for nota in numeros if nota>=5] )    
print(obtener_aprobados())

