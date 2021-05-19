def siguiente_numero():
    num = int(input('Un numero: '))
    num += 1

    #print(f'Siguiente numero: {num}')

    return num

#a = siguiente_numero()
#print(a)

def area_cuadrado(lado):
    result = lado * lado
    return result

#print("El area del cuadrado es:", area_cuadrado(5))


def bienvenida(nombre, apellido, programa):
    print(f"Hola {nombre} {apellido} te inscribiste a {programa}")

    return nombre, apellido, programa

#nombre, apellido, programa = bienvenida("Alan", "Diaz", "JavaScript")

#print(nombre, apellido, programa, sep='\n')

def horas_segundos(horas):
    segundos = horas * 60 * 60
    return segundos

horas = [0, 1, 2]
horas[0] = horas_segundos(1)
horas[1] = horas_segundos(2)
horas[2] = horas_segundos(3)

print(horas)
