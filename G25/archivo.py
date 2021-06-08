from os import close, linesep

""" Lectura """
file = open("fichero.txt", "r")
# texto = file.read()
# print(texto)
# file.close()

# for line in file:
#     print(line)

#linea = file.readline()
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# lineas = list(file)
# file.close()
# print(lineas)

# # for i in lineas:
# #     print(i)

# file = open("fichero.txt", "r")
# lineas_2 = file.readlines()
# file.close()

# print(lineas_2)


""" Escritura """

# print("Valor original fichero")
# rfile = open("fichero.txt", "r")
# texto = rfile.read()
# file.close()
# print(texto)
# print("--insertando linea....\n")
# wfile = open("fichero.txt", "a")
# wfile.write("Nueva linea del ficher\n")
# wfile.close()
# print("nuevo valor dle fichero")
# rfile = open("fichero.txt", "r")
# texto = rfile.read()
# file.close()

cfile = open("fichero_nuevo.txt", "x")
cfile.write("escribiendo sobre fichero. :D")
cfile.close()

rfile = open("fichero_nuevo.txt","r")
info = rfile.read()
rfile.close()
print(info)
