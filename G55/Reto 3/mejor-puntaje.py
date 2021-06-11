"""
EScribir una función retorne la llave con el mayor valor 
-Asumir q odos los valores son enteros
-Si el puntaje no se encuentra, retornar None
-Los stediantes tienen diferentes valores.
-no importar modulos
"""

def mejor_puntaje(diccionario):
    
    max_v = None
    key = None

    if diccionario:
        for k in diccionario:
            if max_v is None:

                max_v = diccionario[k]
                key = k
            elif diccionario[k] > max_v:
                max_v = diccionario[k]
                key = k
        
        return key
    
    return key




estudiantes = {'Alex': 12, 'Arlyn': 20, 'Heynar': 15, 'Robinson': 16, 'Luis': 10}

#print(mejor_puntaje(estudiantes))
print(mejor_puntaje({}))

