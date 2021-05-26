string = str()
lista = list()
tupla = tuple()
diccionario = dict()

#print(string, lista, tupla, diccionario, sep='\n')

datos = {}  # key: value

#print(type(datos))

datos = {"nombre": "Ricky",
        "apellido": "Ricon",
        "Universidad": "utp",
        "Curso": "Python"
         }

# palabra = "Python"
# palabra = "R" + palabra[1:]
# print(palabra)

llave = datos.keys()
valor = datos.values()
llave_valor = datos.items()

# print(valor)
# print(llave)

# print(llave_valor)

estudiante = datos["nombre"] + ' ' + datos["apellido"]

print(datos["Universidad"])

#print(estudiante)