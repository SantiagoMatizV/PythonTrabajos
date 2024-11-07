def conversion_y_comparacion():
  """Convierte grados centígrados a Kelvin, compara números flotantes y muestra el nombre de caracteres."""

  entrada = input("Ingrese un valor: ")

  try:
    # Intenta convertir la entrada a un número entero
    numero_entero = int(entrada)
    # Si es un entero, asumimos que son grados centígrados
    kelvin = numero_entero + 273.15
    print(f"{numero_entero} grados Celsius equivalen a {kelvin} Kelvin.")
  except ValueError:
    try:
      # Si no es un entero, intenta convertirlo a un número flotante
      numero_flotante = float(entrada)
      if numero_flotante > 10.5:
        print(f"{numero_flotante} es mayor que 10.5")
      else:
        print(f"{numero_flotante} no es mayor que 10.5")
    except ValueError:
      # Si no es ni entero ni flotante, asumimos que es un carácter
      print(f"El carácter ingresado es: {entrada}")

# Llamada a la función
conversion_y_comparacion()