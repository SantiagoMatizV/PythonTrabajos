a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

# Encontrar el mayor
mayor = max(a, b, c)

# Encontrar el menor
menor = min(a, b, c)

# Encontrar el medio
medio = (a + b + c) - mayor - menor

print("Los números ordenados de mayor a menor son:")
print(mayor)
print(medio)
print(menor)