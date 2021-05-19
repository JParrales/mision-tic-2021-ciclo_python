#fUNCION QUE SOLICITE UN NUMERO ENTERO AL USUARIO E IMPRIMA EL SIGUIENTE

def siguiente_numero():
    num = int(input('Un numero: '))

    num += 1

    print(f'Siguiente numero: {num}')

    return num

#num = siguiente_numero()

#print(num)

def area_triangulo():
    #el arera de un tirangulo es (base * altura)/2

    base = int(input("base: "))
    altura = int(input("altura"))
    area = base * altura / 2

    print(area)

    return area

#triangulo = area_triangulo()

def area_cuadrado(x):
    
    print(f'{x*x}')
    return x*x

#cuadrado = area_cuadrado(5)

def horas_segundo():
    hora = int(input("Ingrese Hora: "))
    segundos = hora * 60 * 60
    print(hora, 'hora(s) son', segundos, 'segundos.')
    
    return segundos

#valor_segundo = horas_segundo()

def par_mayor_que_100(numero):
    es_mayor = (numero % 2 == 0) and (numero > 100)

    print(f'¿El numero es par mayor que cien?:', es_mayor)

    return numero, es_mayor

#a, b = par_mayor_que_100(50)

#print(a, b)

def es_divisible(num, div):
    divisible = num % div == 0

    print(f'¿El numero {num} es divisible por {div}?: {divisible}')

    return num, div, divisible

numero, divisor, posible = es_divisible(10, 7)

print(numero, divisor, posible)