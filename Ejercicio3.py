sueldo_actual = float(input("Ingrese el sueldo actual del trabajador: "))

if sueldo_actual < 300000:
    aumento = sueldo_actual * 0.15
    sueldo_nuevo = sueldo_actual + aumento
    print("El nuevo sueldo es:", sueldo_nuevo)
else:
    print("El sueldo actual no cumple con los requisitos para el aumento.")