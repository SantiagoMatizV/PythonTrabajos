calificacion1 = float(input("Ingrese la primera calificación: "))
calificacion2 = float(input("Ingrese la segunda calificación: "))
calificación3 = float(input("Ingrese la tercera calificación: "))

menor_calificación = min(calificacion1, calificacion2, calificación3)

calificación_final = (calificacion1 + calificacion2 + calificación3 - menor_calificación) / 2

print("La calificación final es:", calificación_final)