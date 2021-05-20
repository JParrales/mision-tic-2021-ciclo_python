versiones_plone = [2.5, 3.6, 4, 5, 2.5]
# print(versiones_plone)

versiones_plone.append((5,6,7))
#print(versiones_plone)

#print(versiones_plone.count((5,6,7)))

otras_versiones = [5, 6, 7]
versiones_plone.extend(otras_versiones)
# print(versiones_plone)
# print(versiones_plone.index(5, 5))

versiones_plone.insert(2, otras_versiones)
# print(versiones_plone)
#print(len(versiones_plone))
#valor=versiones_plone.pop()
# print(valor)
# print(versiones_plone)

# print(versiones_plone.remove(4))
# print(versiones_plone)

versiones_plone = [(4, 2.5, 5), (4, 3.6, 2.1, 6), (4,4,5)]

# versiones_plone.reverse()
# print(versiones_plone)
versiones_ordenada = versiones_plone.copy()
versiones_ordenada.sort(reverse=True)
