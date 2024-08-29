fecha_nacimiento = input("Introduzca su fecha de nacimiento (dd/mm/aaaa): ")

dia, mes, año = fecha_nacimiento.split('/')

dia = dia.zfill(2)
mes = mes.zfill(2)

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {año}")
