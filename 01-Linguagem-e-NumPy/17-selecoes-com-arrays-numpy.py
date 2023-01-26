import numpy as np

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
dados = np.array([km, anos])

contador = np.arange(10)
print(contador)

item = 6
index = 6 - 1
print(contador[index])

print(dados[1][2]) # dados[1, 2]


# Para fazer um slice no array contador, exibindo os número de 1 a 7
print(contador[1:8])

# Para fazer um slice no array contador, exibindo os número de 1 a 7 em intervalos de 2 (apenas os ímpares)
print(contador[1:8:2])


# Para fazer um slice em um array de duas dimensões
print(dados[ : , 1:4])


km_media = dados[ : , 1:3][0] / (2023 - dados[ : , 1:3][1])
print(km_media)

print(contador > 5)
print(contador[contador > 5])
print(dados[1] > 2000)
print(dados[1] > 2000)
print(dados[ : , dados[1] > 2000])
print(dados[1: , dados[1] > 2000])