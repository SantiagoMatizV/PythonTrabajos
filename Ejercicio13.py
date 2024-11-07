nombre = input("Ingrese el nombre del aprendiz: ")
programa = input("Ingrese el programa de formación: ")
num_actividades = int(input("Ingrese el número de actividades: "))
nota_minima = float(input("Ingrese la nota mínima para aprobar: "))

suma_notas = 0
for i in range(num_actividades):
    nota = float(input(f"Ingrese la nota de la actividad {i+1}: "))
    suma_notas += nota

nota_final = suma_notas / num_actividades

if nota_final >= nota_minima:
    print(nombre, " aprobó el programa ", programa)
else:
    print(nombre, " reprobó el programa ", programa)