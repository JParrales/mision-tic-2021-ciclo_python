objetos = {

    'Mark I': {
        'color': 'Gris',
        'material': 'metal',
        'peso kg': 360,
        'sistema': 'MS-DOS',
        'disponible': False
    }
}

# print(objetos['Mark I'])

# print('Mark I' in objetos)

# nombre = "Daniel"
# apellido = "Vesga"

# print(nombre + apellido)


name = "Jose Parrales" 
sep = name.index(' ')
name = name[:sep]
surname = name[sep +1: ]

print(name)
print(surname)


nombre = 'Jose PArraLES'
sep = nombre.index(' ')
name = nombre[:sep]
last_name = nombre[sep +1: ]

print(name)
print(last_name) 