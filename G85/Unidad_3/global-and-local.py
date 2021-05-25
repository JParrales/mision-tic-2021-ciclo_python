saludo = 'hola'
print(saludo)

def local():
    global saludo
    print(saludo)
    
    saludo = 'python'
    print(saludo)


local()
print(saludo)