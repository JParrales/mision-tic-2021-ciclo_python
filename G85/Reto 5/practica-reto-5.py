import numpy as np
import pandas as pd

archivo = pd.read_csv(
    'https://raw.githubusercontent.com/JParrales/mision-tic-2021-ciclo_python/master/G25/Reto%205/notas.csv')

archivo['PUNTAJE'] = archivo['MATEMATICA'] + archivo['LENGUAJE'] + \
    archivo['CIENCIAS'] + archivo['CIUDADANAS'] + archivo['IDIOMAS']

by_puntaje = archivo.sort_values('PUNTAJE', ascending=False).head()
tabla_1 = by_puntaje[['ESTUDIANTE', 'PUNTAJE']]
puestos = [1,2,3,4,5]
tabla_1 = by_puntaje.set_index(np.array(puestos))
tabla_1.index.name = 'PUESTO'

promedio = archivo.mean()
promedio.round(2)

tabla_2 = pd.DataFrame(promedio)

tabla_2.columns = ['PROMEDIO']
tabla_2.index.name = 'PRUEBAS'

print(tabla_1)
print(tabla_2)