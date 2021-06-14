""" 
-llevar el control de compras en el supermacado.
construir función q reciba en un diccionario 
el producto y su valor , de las compras realizadas.
Retornar el STIRNG del nombre del porducto de mayor valor
o los nombres de los productos mas cosotosos,
si no he comprado retornar "No hay productos comprados"

"""

compras = {
    "arroz" : 1200,
    "lentejas" : 15000,
    "lechex 6" : 1200,
    "mecatos" : 15000,
    "carne" : 15000,
    "pescado" : 14000
}


vacio = {}
def carrito(mercado: dict) -> str:

    if mercado:

        valores = list(mercado.values())
        mayor = max(valores)
        llaves = [k for k in mercado if mercado[k] == mayor]

        # for key, value in mercado.items():

        #     if value == mayor:
        #         llaves.append(key)
        
        return ', '.join(llaves)
    
    return "No hay productos comprados"

print(carrito(compras))
