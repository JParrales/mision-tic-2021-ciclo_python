#versiones = dict(python=2.7*2, zope=2.13, plone=5.1, django=2.1)

# print(versiones)
# print(versiones.clear())
# print(versiones)

# versiones2 = versiones
# new_version = versiones.copy()
# print(versiones)
# print(new_version)
# print(id(versiones))
# print(id(versiones2))
# print(id(new_version))

# secuencia = ('python', 'zope', 'plone')
# versiones =  dict.fromkeys(secuencia, "python")
versiones = dict(python=2.7, zope=2.13, plone=5.1)
#print(versiones)

#print(versiones.get('zxx', "el valor no se encontro"))

#del versiones['python']
#print(versiones)

# print(versiones.pop('zope'))
# print(versiones)

versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones)
versiones_adicional = dict(django=2.1)
print(versiones_adicional)

print(versiones.update(versiones_adicional))
print(versiones)

