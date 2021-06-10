""" 

• Crear un objeto en la base de datos con sus especificaciones,
esto se realizará a través de un diccionario.
• Al intentar crear un objeto que ya se encuentre en la base de datos, 
solo verificará su existencia.
• Si un objeto se encuentra en la base de datos y sus especificaciones no coinciden 
la función debe actualizar el objeto en la base de datos.
• La llave con la cual se identificará el objeto será de tipo string, 
si el tipo de la llave es diferente, debe solicitar un identificador válido para el objeto.
"""
# print(clientes[cliente]) 
# print(clientes[cliente["nombre"]]) 
def bd_objetos():

    objetos = {

        'Mark I': {
            'color': 'Gris',
            'material': 'metal',
            'peso kg': 360,
            'sistema': 'MS-DOS',
            'disponible': False
        },
        'Mark II': {
            'color': 'Gris',
            'material': 'metal',
            'peso kg': 280,
            'sistema': 'JARVIS',
            'disponible': True
        },
        'Mark III': {
            'color': 'Rojo Y Oro',
            'material': 'oro y titanio',
            'peso kg': 280,
            'sistema': 'JARVIS',
            'disponible': True
        },
        'Mark VII': {
            'color': 'Rojo Y Oro',
            'material': 'oro y titanio',
            'peso kg': 200,
            'sistema': 'JARVIS',
            'disponible': False
        },
        'Veronica I': {
            'color': 'Rojo Y Oro',
            'material': 'acero, hierro y niquel',
            'peso kg': 975,
            'sistema': 'JARVIS',
            'disponible': True
        },
    }

    return objetos

