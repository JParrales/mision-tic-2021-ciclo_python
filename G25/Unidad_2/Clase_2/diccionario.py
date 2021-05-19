string = str()
lista = list()
tupla = tuple()
diccionario = dict()

#print('' is string, lista, tupla, diccionario, sep='\n')

diccionario = {}  # {key: value}
# print(diccionario)

datos = {"nombre": "Ricky",
         "apellido": "Ricon",
         "Universidad": "UTP",
         "Curso": "Python"}

llave = datos.keys()
valor = datos.values()
#print(llave, valor, sep='\n')

estudiante_1 = datos["nombre"] + ' ' + datos["apellido"]
#print(estudiante_1)

equipos_liga_aguila = {}

print(equipos_liga_aguila)

equipos_liga_aguila['Nacional'] = 14
equipos_liga_aguila['America'] = 12

print(equipos_liga_aguila)
