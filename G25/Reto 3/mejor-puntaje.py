"""
Escribir una función que retorne la llave con el mayor valor.
-Los valores serán de tipo enteros
-si un valor no se en cuentra, retornar None
-Las claves tienen diferentes valores

"""

def mejor_valor(diccionario):
    mayor = None
    key = None

    if diccionario:

        for k in diccionario:
            if mayor is None:
                mayor = diccionario[k]
                key = k
            elif diccionario[k]> mayor:
                mayor = diccionario[k]
                key = k
        
        return key
    
    return key


asistencia = {'Cindy': 8, 'Fabian': 15, 'Juan': 17, 'Laura': 10, 'Diego': 6}

print(mejor_valor(asistencia))

