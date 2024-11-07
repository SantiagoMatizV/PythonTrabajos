numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Encontrar el mayor y el menor
mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

# Calcular el número medio
medio = numero1 + numero2 + numero3 - mayor - menor

print("El número medio es:", medio)