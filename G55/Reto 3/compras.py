""" 
-llevar el control de compras en el supermacado.
construir función q reciba en un diccionario 
el producto y su valor , de las compras realizadas.
Retornar el STIRNG del nombre del porducto de mayor valor
o los nombres de los productos mas cosotosos,
si no he comprado retornar "No hay productos comprados"

"""

mercado = {
    "arroz": 1200,
    "aceite": 12000,
    "12na de huevos": 1800,
    "carne": 12000,
    "pescado": 12000,
    "chocolate": 8000,
    "pollo": 8000
}

diccionario_vacio = {
    
}


def compras(diccionario: dict) -> str:

    if diccionario:
        valores = list(diccionario.values())
        mayor = max(valores)
        llaves = []

        for key, value in diccionario.items():

            if value == mayor:
                llaves.append(key)
        
        return ', '.join(llaves)
    
    else:
        return "No hay productos comprados"


print(compras(mercado))
#print(compras(diccionario_vacio))