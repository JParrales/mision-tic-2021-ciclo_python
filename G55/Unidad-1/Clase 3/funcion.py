""" def nombre(arg1, arg2, ...):
    instruc1
    instruc1
    ...
    
    return

 """

def mensaje():
   x = "Hola {nombre}, estas en el curso de python"

   return x

#print(mensaje())


def cuadrado(numero):
    return numero*numero

print(cuadrado(9))


def numbre_completo(nombre = input("Escribe el nombre:"), apellido = input("Escribe el apellido: ")):
    print(f"{nombre} {apellido}")

    return nombre, apellido

nombre, apellido = numbre_completo()


#print(nombre, apellido)