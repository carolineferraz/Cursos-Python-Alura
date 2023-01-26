import numpy as np

# km = [44410., 5712., 37123., 0., 25757.]
# anos = [2003, 1991, 1990, 2019, 2006]

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

idade = 2023 - anos
print(idade)

km_media = km / idade
print(km_media)


dados = np.array([km, anos])
print(dados)
print(dados.shape)


km_media = dados[0] / (2023 - dados[1])
print(km_media)