def divisores(numero):
    divisor = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisor.append(i)
    
    return divisor


if __name__ == '__main__':

    num = int(input("Ingrese un numero: "))
    print(divisores(num))
    print("---FIN PROGRAMA")