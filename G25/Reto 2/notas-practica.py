

data = {
    16361910: {
        'nombre': 'MONTY',
        'apellido': 'BURNS',
        'direccion': 'mansion burns',
        'telefono': 24275370,
        'membresia': True
    },
}


actualizar = {
    1234567: {
        'nombre': 'bart',
        'apellido': 'simpson',
        'direccion': 'mansion burns',
        'telefono': "n/a",
        'membresia': True
    }
}

# cliente = 16361910

# print(data[cliente])

# data[cliente] = actualizar[cliente]

# print(data[cliente])

#print(data)
#print(data[16361910])
#print(data[16361910]['nombre'])

cliente = 'monty burns'
# sep_idx = cliente.index(' ')
# print(sep_idx)

# nombre = cliente[:sep_idx]
# print(nombre)
# apellido = cliente[sep_idx + 1:]
# print(apellido)

#print(16361910 in data)

print(data)

print('='*25)

data.update(actualizar)

print(data)