""" 
-Crear un cliente en la base de datos con sus especificaciones,
esto se realizará a través de un diccionario. 
- Verificar si el cliente ingresado se encuentra en la base de datos.
f"El cliente {cliente} Se encuentra en la base de datos"
- Si un cliente se encuentra en la base de datos y sus datos de contacto y/o membresía no
coinciden, debe actualizar los datos. 
f"Cliente {cliente}, actualizado en la base de datos"
- El cliente será identificado con un numero entero, si el tipo de dato no coincide debe solicitar
un id valido. 
f"Ingrese un id de tipo valido."
- Si el cliente no se encuentra en la base de datos, actualizarla.
f"El cliente {cliente} se agregó a la base de datos."
"""


def bd_clientes():

    clientes = {

        34043243: {
            'nombre': 'HOMERO',
            'apellido': 'SIMPSON',
            'direccion': 'avenida siempreviva 742',
            'telefono': 46637600,
            'membresia': False
        },
        42140704: {
            'nombre': 'MARGE',
            'apellido': 'SIMPSON',
            'direccion': 'siempreviva',
            'telefono': 46637600,
            'membresia': True
        },
        21015602: {
            'nombre': 'NED',
            'apellido': 'FLANDERS',
            'direccion': 'avenida siempreviva 864',
            'telefono': 63392730,
            'membresia': True
        },
        26677308: {
            'nombre': 'MOU',
            'apellido': 'SZYSLAK',
            'direccion': 'calle wualnut 668',
            'telefono': 76484377,
            'membresia': False
        },
        16361910: {
            'nombre': 'MONTY',
            'apellido': 'BURNS',
            'direccion': 'mansion burns',
            'telefono': 24275370,
            'membresia': True
        },
    }

    return clientes


def reto_2(cliente: int, nombre: str, direccion: str, telefono: int, miembro: bool, bd_clientes: dict) -> dict:

    if type(cliente) is not type(int()):
        return f"Ingrese un id de tipo valido."
    
    datos = {}
    nombre = nombre.upper()
    sep_idx = nombre.index(' ')

    datos[cliente] = {
        'nombre': nombre[:sep_idx],
        'apellido': nombre[sep_idx + 1:],
        'direccion': direccion.lower(),
        'telefono': telefono,
        'membresia': miembro,
    }

    if cliente in bd_clientes:
        if bd_clientes[cliente] != datos[cliente]:
            bd_clientes[cliente] = datos[cliente]

            return f"Cliente {cliente}, actualizado en la base de datos"

        return f"El cliente {cliente} Se encuentra en la base de datos"
    
    else:
        bd_clientes.update(datos)
        return f"El cliente {cliente} se agregó a la base de datos."
    


clientes = bd_clientes()
print(reto_2(34043243, 'Homero Simpson',
      'AVENIDA SIEMPREVIVA 742', 46637600, False, clientes))
print(clientes.get(34043243, 'Ciente no se encuentra en BD.'))

# El cliente 34043243 Se encuentra en la base de de datos
#{'nombre': 'HOMERO', 'apellido': 'SIMPSON', 'direccion': 'avenida siempreviva 742', 'telefono': 46637600, 'membresia': False}

clientes = bd_clientes()
print(reto_2(42140704, 'marge simpson', 'avenida siempreviva 742', 46637600, True, clientes))
print(clientes.get(42140704, 'Ciente no se encuentra en BD.'))

# Cliente 42140704, actualizado en la base de datos
# {'nombre': 'MARGE', 'apellido': 'SIMPSON', 'direccion': 'avenida siempreviva 742', 'telefono': 46637600, 'membresia': True}

clientes = bd_clientes()
print(reto_2('cc24687900', 'pepito perez', 'CL Perezlandia ESQ.', 3036052, True, clientes)) 
print(clientes.get('24687900', 'Ciente no se encuentra en BD.'))


clientes = bd_clientes()
print(reto_2(24687900, 'pepito perez', 'CL Perezlandia ESQ.', 3036052, True, clientes)) 
print(clientes.get('24687900', 'Ciente no se encuentra en BD.')) 

# Respuesta:
# Ingrese un id de tipo valido.
# Ciente no se encuentra en BD.