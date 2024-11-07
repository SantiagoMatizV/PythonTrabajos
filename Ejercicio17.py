numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if numero1 % numero2  == 0:
    print(numero1, " es divisible por ", numero2)
elif numero1 % numero3 == 0:
    print(numero1, " es divisible por ", numero3)
elif numero2 % numero1 == 0:
    print(numero2, " es divisible por ", numero1)
elif numero2 % numero3 == 0:
    print(numero2, " es divisible por ", numero3)
elif numero3 % numero1 == 0:
    print(numero3, " es divisible por ", numero1)
elif numero3 % numero2 == 0:
    print(numero3, " es divisible por ", numero2)
else:
    print("Ningún número es divisible entre los demás")