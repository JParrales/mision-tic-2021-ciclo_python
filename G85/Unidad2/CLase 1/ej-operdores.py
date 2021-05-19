#Funcion que solicite un numero entero y luego imprima el siguiente:

def siguiente_numero():
    num = int(input('Un numero: '))

    num += 1

    print(f'Siguiente numero: {num}')

    return num

#num = siguiente_numero()

#print(num)

def area_triangulo():
    #el area del triangulo es (base * altura)/2

    base = int(input("base: "))
    altura = int(input("altura: "))
    area = base * altura / 2

    return area

#triangulo = area_triangulo()

#print(triangulo)

def area_cuadrado(x):
    print(x*x)

#area_cuadrado(5)


""" def horas_segundo(horas=int(input("Horas: "))):
    segundos = horas * 60 * 60
    print(horas, 'hora(s) son', segundos, 'segundos.')

    return segundos """

#valor_segundo = horas_segundo(5)


def par_mayor_10(numero):
    es_mayor = (numero % 2 == 0) and (numero > 10)

    print(f'¿El numero es par mayor a 10?:', es_mayor)

    return numero, es_mayor

num, cumple_condicion = par_mayor_10(17)

print(num, cumple_condicion)