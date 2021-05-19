import funciones_calc as calc


def calculadora(num1: int, num2: int, operacion: str) -> int:
    if operacion == '+':
        result = calc.suma(num1, num2)
    elif operacion == '-':
        result = calc.resta(num1, num2)
    elif operacion == '/':
        if num2 == 0:
            result = 'Division x 0 no está definida'
        else:
            result = calc.division(num1, num2)
    else:
        result = calc.multiplicacion(num1, num2)
    
    return result

calculo = calculadora(5, 0, '/')

print(calculo)

