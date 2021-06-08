from typing import List
import numpy as np

#crear vector de 5 elementos

lista = [25, 12, 15, 66, 12]
vector = np.array(lista)
print(vector)

print(vector + 1)
print(vector * 5)

print(np.sum(vector))
print(np.mean(vector))

print(vector + vector)