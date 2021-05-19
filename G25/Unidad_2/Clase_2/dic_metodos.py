versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
#print(versiones)

# versiones.clear()
# print(versiones)

new_version = versiones.copy()
# print(id(versiones))
# print(id(new_version))

# print(new_version == versiones)
# print(new_version is versiones)

# new_version.clear()
# print(id(new_version))
# print(id(new_version))

secuencia = ('python', 'zope', 'plone')
versiones = dict.fromkeys(secuencia, [i for i in range(3)])

# print(versiones)
# print(secuencia)

# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones.get('plone'))
# print(versiones.get('java', "no se encontro valor"))

versiones = dict(python=2.7, zope=2.13, plone=5.1)
#print(versiones.items()

# del versiones["plone"]
# print(versiones)

# valor = versiones.pop('python')
# print(valor)
# print(versiones)

versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones)

versiones_adicional = dict(django=2.1)
print(versiones_adicional)

versiones.update(versiones_adicional)
print(versiones)