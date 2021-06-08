nombre = 'Fernando Nicolai Ascencio Vanegas'
apellido_1 = 'Ascencio'

# print(apellido_1 in nombre)

datos_1 = {
    'nombre': 'Julian',
    'apellido': 'Matinez' 
}

datos_2 = {
    'nombre': 'Juliana',
    'apellido': 'Matinez' 
}

# print(datos_1['nombre'] ==  datos_2['nombre'])


numeros = ['1-2-3-4-5', '1-2*3#4/5']

print(numeros[0].index('-'))
print(numeros[1].index('*'))

numeral = numeros[1].index('#')
print(numeral)
numeros[1] = numeros[1][:numeral] + ' ' + numeros[1][numeral + 1:]
print(numeros)