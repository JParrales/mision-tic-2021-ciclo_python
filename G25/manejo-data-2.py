

corredores = {
    'Usain Bolt': {
        '100m': 9.63,
        '200m': 19.52,
        '4x100m': 36.48
    },
    'Tayson Gray': {
        '100m': 9.73,
        '200m': 19.52,
        '4x100m': 37.23
    },
    'Yohan Blake': {
        '100m': 9.73,
        '200m': 22.52,
        '4x100m': 35.48
    },
}


"""
lista de listas: los resultados de las pruebas de c/u de los participantes
Matriz: los resultados de las pruebas
Promedios de tiempo en cada prueba
tiempo total:
si en el tiempo es mayor a 40 dar un tiempo de 39.9
lista de participantes. *
nombre del ganador
"""
import numpy as np
from numpy.lib.function_base import _parse_gufunc_signature

participantes = [] #['Usain Bolt', 'Tayson Gray', 'Yohan Blake']

for i in corredores.keys():
    participantes.append(i)

print(participantes)

pruebas = [] #['100m', '200m', '4x100m']

for i in corredores[participantes[0]].keys():
    pruebas.append(i)

print(pruebas)

resultados = []
# [[9.63, 19.52, 36.48], [9.73, 19.52, 37.23], [9.73, 22.52, 35.48]]


for i in participantes:
    resultados_corredor = []
    for x in pruebas:
        resultados_corredor.append(corredores[i][x])
    
    resultados.append(resultados_corredor)

print(resultados)

