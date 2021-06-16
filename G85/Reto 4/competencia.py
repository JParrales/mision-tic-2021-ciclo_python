corredores = {
    'Usain Bolt': {
        '100m': 9.63,
        '200': 19.52,
        '4x100': 36.48
    },
    'Tayson Gray': {
        '100m': 9.73,
        '200': 19.52,
        '4x100': 42.55
    },
    'Yahan Blake': {
        '100m': 9.73,
        '200': 52.52,
        '4x100': 35.48
    }
}

"""
lista de participantes
lista de listas. resultados de cada prueba x participante
si el tiempo de una prueba es mayor a 40s dar un tiempo 39.99
Matriz: los resultados de todas las pruebas (normalizadas)
tiempo promedio por pureba
tiempo total de cada participante
nombre del ganador.
"""
import numpy as np

participantes = list(corredores.keys())
resultados = [list(corredor.values()) for corredor in corredores.values()]
normalizar = [list(map(lambda res: 39.99 if res >= 40 else res, i)) for i in resultados]
matriz = np.array(normalizar)
promedio = np.around(np.average(matriz, axis=0), decimals=1)
t_total = np.sum(matriz, axis=1)
ganador = participantes[t_total.argmin()]


print(participantes)
print(resultados)
print(normalizar)
print(matriz)
print(promedio)
print(t_total)
print(ganador)

#participantes = [i for i in corredores.keys()]

# for i in corredores:
#     participantes.append(i)

# for i in participantes:
#     resultados_corredor = []
#     for x in corredores[i].values():
#         resultados_corredor.append(x)
#     resultados.append(resultados_corredor)

#resultados = [[resultado for resultado in corredor.values()] for corredor in corredores.values()]

# idx_i = 0
# for i in resultados:
#     idx_j = 0
#     for j in i:
#         if j >= 40:
#             resultados[idx_i][idx_j] = 39.99
#         idx_j += 1
#     idx_i += 1