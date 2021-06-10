""" 

- Verificar si el cliente ingresado se encuentra en la base de datos.
- Si un cliente se encuentra en la base de datos y sus datos de contacto y/o membresía no
coinciden, debe actualizar los datos.
- El cliente será identificado con un numero entero, si el tipo de dato no coincide debe solicitar
un id valido.
- Si el cliente no se encuentra en la base de datos, actualizarla.
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
    pass


data = bd_clientes()
print(data[21015602])