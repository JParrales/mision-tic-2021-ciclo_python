versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)

# print(versiones)
# versiones.clear()
#print(versiones)

new_version = versiones

# print(versiones)
# print(id(versiones))
# print(new_version)
# print(id(new_version))



# secuencia = [1, 2, 3]
# versiones = dict.fromkeys(secuencia, 3)  #[i for i in range(10)])

# print(secuencia)
# print(versiones)

versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
# # print(versiones['python'])
# # print(versiones.get('java', 'no se encontro'))
# print(versiones)

# del versiones['django']
# print(versiones)
val = versiones['plone']
valor = versiones.pop('plone')

# print(val)
# print(valor)


versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones)
versiones_extra = dict(ruby=2.7)

versiones.update(versiones_extra)

print(versiones)