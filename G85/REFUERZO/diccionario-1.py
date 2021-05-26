""" Escribir un programa que guarde en una variable 
el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo 
o un mensaje de aviso si la divisa no está en el diccionario. """

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
#divisas = dict(Euro = '€', Dollar = '$', Yen = '¥')

# print(monedas)
# print(divisas)
# print(monedas == divisas)

def divisas(monedas):
    tipo_moneda = input('Ingrese divisa: ').title()
    print(tipo_moneda)
    print(monedas.get(tipo_moneda, 'no se reconoce la divisa'))

divisas(monedas)

#FUNCION YISNEY
def divisas():
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    ndivisa = input("¿Qué símbolo de divisa deseas consultar?: ").title() 
    #Método title() vuelve la primera letra mayúscula
    if ndivisa in divisas:
        print(f"El símbolo de la divisa {ndivisa} es {divisas[ndivisa]}.")
    else:
        print("La divisa no se encuentra en el diccionario.")

divisas() 


