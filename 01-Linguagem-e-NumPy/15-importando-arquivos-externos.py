import numpy as np 

# Importando arquivos externos:
km = np.loadtxt('01-Linguagem-e-NumPy/data/carros-km.txt', dtype=int)
print(km)
print(km.dtype)
print(km.shape)

anos = np.loadtxt('01-Linguagem-e-NumPy/data/carros-anos.txt', dtype=int)
print(anos)

km_media_anual = km / (2023 - anos)
print(km_media_anual)
print(type(km_media_anual))