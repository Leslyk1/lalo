telefono = input("Introduce ell número de télefono con el formato +34-número-extensión: ")

partes = telefono.split('-')

numero = partes[1]

print(f"El número sin el prefijo y la extensión es: {numero}")
