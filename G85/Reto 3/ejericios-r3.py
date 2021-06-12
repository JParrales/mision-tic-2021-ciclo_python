""" 
-llevar el control de compras en el supermacado.
construir funicion q reciba en un diccionario 
el producto y su valor , de las compras realizadas.
Retornar el STIRNG del nombre del porducto de mayor valor
o los nombres de los productos mas cosotosos,
si no he comprado retornar "No hay productos comprados"

"""

productos = {
    "cereal": 3000,
    "bananas": 6000,
    "huevos 12na": 1800,
    "aceite": 5000,
    "pescado": 6000,
    "pizza": 6000
}
alacena = {

}

def compras(diccionario: dict) -> str:
    
    #diccionatio vacio = False, lleno = True
    if diccionario:

        valores = list(diccionario.values())
        max_v = max(valores)
        llaves = []

        for key, value in diccionario.items():

            if max_v == value:
                llaves.append(key)
        
        return ', '.join(llaves)
    
    return "No hay productos comprados"


compra = compras(productos)
print(compras(productos))

#print(compras(alacena))




        
