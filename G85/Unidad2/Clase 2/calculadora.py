import funciones_calc as calc


def calculadora(num1: int, num2: int, operador: 'str') -> int:
    if operador == '+':
        out = calc.suma(num1, num2)
    elif operador == '-':
        out = calc.resta(num1, num2)
    elif operador == '/':
        if num2 != 0:
            out = calc.dividir(num1, num2)
        else:
            out = 'div / 0, no está definida'
    else:
        out = calc.multiplicar(num1, num2)
    
    return out

calcular = calculadora(3, 0, '/')

print(calcular)