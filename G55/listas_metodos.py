numeros = [0, 1, 2 , 3]

numeros2 = numeros[:]
numeros2[-1] = 10

numeros.append(25)

# print(numeros)
# print(numeros2)

versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]

#print("3.6 ->", versiones_plone.count(3.6))

otras_versiones = [5, 6, 7, 8]

versiones_plone.extend(otras_versiones) 
# print(versiones_plone)
versiones_plone.append(otras_versiones)
#print(versiones_plone)

# print(versiones_plone.index(6, 6))
versiones_plone.insert(2, otras_versiones)
#print(versiones_plone)

#print(versiones_plone.pop())
# print(versiones_plone)

#versiones_plone.remove(6)

versiones_plone = [4, 2.5, 5, 3.6, 2.1, 6]
print(versiones_plone)

#versiones_plone.sort(reverse=True)
#print(versiones_plone)

versiones_plone.reverse()
print(versiones_plone)