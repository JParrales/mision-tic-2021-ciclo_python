semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
#print(len(semana))
#print(semana[0], semana[1], semana[2])

dia_laborales = semana[0:5]
#print(dia_laborales)

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

primeros10 = numeros[0:11]
#print(primeros10)

pares = numeros[::2] #[0:22:2]
impares = numeros[1::2]
ultimo = numeros[-1]
desendendte = numeros[::-1]

print(pares)
print(impares)
print(ultimo)
print(desendendte)

lenguaje = "Python"

print(lenguaje[::-1])