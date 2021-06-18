import pandas as pd
import numpy as np

link = 'https://raw.githubusercontent.com/JParrales/mision-tic-2021-ciclo_python/master/G85/Reto%205/resultados.csv'
archivo = pd.read_csv(link)

archivo['PUNTAJE'] = archivo['MATEMATICA'] + archivo['LENGUAJE'] + \
    archivo['CIENCIAS'] + archivo['CIUDADANAS'] + archivo['IDIOMAS']

tabla_1 = archivo[['ESTUDIANTE', 'PUNTAJE']]
by_estudiante = archivo.sort_values('ESTUDIANTE')
by_puntaje = tabla_1.sort_values('PUNTAJE', ascending=False).head()

puesto = [1,2,3,4,5]
tabla_1 = by_puntaje.set_index(np.array(puesto))
tabla_1.index.name = 'PUESTO'
print(tabla_1)
print()

tabla_2 = pd.DataFrame(archivo.mean().round(2))
#dicc =tabla_2.to_dict()
tabla_2.index.name = 'PRUEBAS'
tabla_2.columns = ['PROMEDIO']
tabla_2['DESVIACION'] = pd.DataFrame(archivo.std().round(2))


print(tabla_2)
