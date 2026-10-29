#indica cuantos alumnos han aprobado
notas_alumnos=[6.4,2.9,5.5,8.0,3.1,7.2] 
aprobados=0
for num in notas_alumnos:
    if num>=5:
        aprobados=aprobados+1
print("total aprobados", aprobados)

"""
mayor=notas_alumnos[0] 
for nota in notas_alumnos:
    if nota>mayor:
        mayor=nota
print(f"Nota mas alta{mayor}", aprobados)
"""

print(f"la nota mas alta es {max(notas_alumnos)}")
print(f"la nota mas baja es {min(notas_alumnos)}")
print(f"la nota ordenada es {sorted(notas_alumnos, reverse=True)}")
