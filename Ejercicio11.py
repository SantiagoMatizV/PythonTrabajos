longitud = float(input("Ingrese la longitud de la varilla (cm): "))
diametro = float(input("Ingrese el diámetro de la varilla (cm): "))

densidad = 3.5
masa = (diametro * longitud) / densidad

if (longitud > 7.5 and longitud <= 9) and (diametro >= 0.5 and diametro <= 1.3) and (masa <= 5.8):
    print("La pieza es aceptada")
else:
    print("La pieza es rechazada")