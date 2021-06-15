

corredores = {
    'Usain Bolt': {
        '100m': 9.63,
        '200m': 19.52,
        '4x100m': 36.48
    },
    'Tayson Gray': {
        '100m': 9.73,
        '200m': 19.52,
        '4x100m': 42.55
    },
    'Yohan Blake': {
        '100m': 9.73,
        '200m': 22.52,
        '4x100m': 35.48
    },
}


"""
lista de participantes. *
lista de listas: los resultados de las pruebas de c/u de los participantes *
si en el tiempo es mayor a 40 dar un tiempo de 39.9 *
Matriz: los resultados de las pruebas ( aplicada la condicion) *
Promedios de tiempo en cada prueba *
tiempo total por participante: *
nombre del ganador *
"""
import numpy as np


participantes = [] #['Usain Bolt', 'Tayson Gray', 'Yohan Blake']

for i in corredores.keys():
    participantes.append(i)

#print(participantes)

pruebas = [] #['100m', '200m', '4x100m']

for i in corredores[participantes[0]].keys():
    pruebas.append(i)

#print(pruebas)

resultados = []
# [[9.63, 19.52, 36.48], [9.73, 19.52, 37.23], [9.73, 22.52, 35.48]]


for i in participantes:
    resultados_corredor = []
    for x in pruebas:
        resultados_corredor.append(corredores[i][x])
    
    resultados.append(resultados_corredor)

#print(resultados)

normalizar = []

for i in resultados:

    normalizados = list(map(lambda valor: 39.9 if valor > 40 else valor, i))
    normalizar.append(normalizados)

#print(normalizar)

matriz = np.array(normalizar)
print(matriz)
print()
promedio = np.average(matriz, axis=0)
promedio = np.around(promedio, decimals=1)
print(promedio)

t_total = np.sum(matriz, axis=1)
print(t_total)

ganador = participantes[t_total.argmin()]
print(ganador)