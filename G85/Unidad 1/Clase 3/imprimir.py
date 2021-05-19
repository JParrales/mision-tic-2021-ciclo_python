def hola_mundo():
    print("Hola Mundo")

hola_mundo()

def crear_mensaje(nombre):
    mensaje = "Hola {}, bienvenido al curso de Python".format(nombre)
    #mensaje = f"Hola {nombre}, bienvenido al curso de Python"

    return mensaje

nombre = "Jose"
# print(crear_mensaje("Jose"))
# print(f"Hola {nombre}, bienvenido al curso de Python")

