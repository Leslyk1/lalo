correo = input("Introduzca su correo electrónico: ")

nombre_usuario = correo.split('@')[0]

nuevo_correo = f"{nombre_usuario}@ceu.es"

print(f"Su nuevo correo es: {nuevo_correo}")
