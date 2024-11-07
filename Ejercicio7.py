nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo (M/F): ").upper()
estado_civil = input("Ingrese el estado civil (C/S): ").upper()

if (sexo == 'M' and estado_civil == 'C' and edad > 40) or (sexo == 'F' and estado_civil == 'S' and edad < 50):
    print(nombre, "Tiene", edad,"Genero", sexo,"Se encuentra", estado_civil)