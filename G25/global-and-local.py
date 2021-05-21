saludo = 'hola'

def local():
    global saludo
    print(saludo)
    saludo = 'hola variable local'
    print(saludo)

local()
print(saludo)