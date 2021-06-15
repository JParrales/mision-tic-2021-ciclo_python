"""
lista de participantes.
lista de listas: los resultados de las pruebas de c/u de los participantes
si en el tiempo es mayor a 40 dar un tiempo de 39.9
Matriz: los resultados de las pruebas ( aplicada la condicion)
Promedios de tiempo en cada prueba *
tiempo total por participante: *
nombre del ganador *
"""
# rsultados = [[9.63, 19.52, 36.48], [9.73, 19.52, 42.55]. [9.73, 22.52, 35.48]]
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


import numpy as np



participantes = list(corredores.keys())
resultados = []

for i in participantes:
    resultados_corredor = []
    for x in corredores[i].values():
        resultados_corredor.append(x)
    
    resultados.append(resultados_corredor)

print(participantes)
print(resultados)

normalizar = []

for i in resultados:

    datos_normalizados = list(map(lambda valor: valor if valor <= 20 else 19.9, i))
    normalizar.append(datos_normalizados)

#print(normalizar)

matriz = np.array(normalizar)
print(matriz)

promedio = np.average(matriz, axis=0)
promedio = np.around(promedio, decimals=1)
print(promedio)

t_total = np.sum(matriz, axis=1)
print(t_total)

# ganador_idx = t_total.argmin()
# print(ganador_idx) 

ganador = participantes[t_total.argmin()]
print(ganador)


#participantes = [i for i in corredores.keys()]
# for i in corredores.keys():
#     participantes.append(i)

#print(participantes)
