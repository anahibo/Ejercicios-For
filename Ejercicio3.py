numero_tabla = int(input("Ingrese el número: "))
print("Tabla del", numero_tabla)
for i in range(12):
    multiplicador = i + 1
    resultado = numero_tabla * multiplicador
    print(numero_tabla, "x", multiplicador, "=", resultado)