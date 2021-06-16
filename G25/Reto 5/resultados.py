import pandas as pd
import numpy as np

archivo = pd.read_csv('25-listado-clases.csv')


# Calcular Puntaje
archivo['PUNTAJE'] = archivo['MATEMATICA'] + archivo['LENGUAJE'] + \
    archivo['CIENCIAS'] + archivo['CIUDADANAS'] + archivo['IDIOMAS']

# Organizar Alfabeticamente

by_estudiante = archivo.sort_values('ESTUDIANTE')

# cuadro de honor
by_puntaje = archivo.sort_values('PUNTAJE', ascending=False).head()
by_puntaje = by_puntaje[['ESTUDIANTE', 'PUNTAJE']]
puestos = [1, 2, 3, 4, 5]
posiciones = by_puntaje.set_index(np.array(puestos))
posiciones.index.name = 'PUESTO'
promedio = archivo.mean().round(2)
print(promedio)

# print(by_estudiante)
