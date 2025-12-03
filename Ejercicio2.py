suma = 0
for i in range(10):
    calificacion = float(input("Ingrese la calificacion: "))
    suma = suma + calificacion
promedio = suma / 10
print("Sumatoria total:", suma)
print("Promedio final:", promedio)