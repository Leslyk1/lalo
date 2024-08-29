precio = input("Introduzca el precio del producto en euros (con dos decimales): ")

euros, centimos = precio.split('.')

print(f"El precio tiene {euros} euros y {centimos} centimos.")
