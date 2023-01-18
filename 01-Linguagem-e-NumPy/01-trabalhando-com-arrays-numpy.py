import numpy as np

km = np.loadtxt('./data/carros-km.txt', dtype=int)
print(km)

anos = np.loadtxt('./data/carros-anos.txt', dtype=int)
print(anos)

km_media_anual = km / (2023 - anos)
print(km_media_anual)
print(type(km_media_anual))