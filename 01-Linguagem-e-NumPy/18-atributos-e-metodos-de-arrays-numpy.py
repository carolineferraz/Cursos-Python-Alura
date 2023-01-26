import numpy as np

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
dados = np.array([km, anos])

print(dados)

# Retorna uma tupla com as dimensões do array
print(dados.shape)

# Retorna o número de dimensões do array
print(dados.ndim)

# Retorna o número de elementos do array
print(dados.size)

# Retorna o tipo de dado dos elementos do array
print(dados.dtype)

# Retorna o array transposto (converte linhasem colunas e vice versa)
print(dados.T) # print(dados.transpose())

# Retorna o array numpy como uma lista python
print(dados.tolist())

# Retorna um array que contém os mesmos dados mas com uma nova forma (modifica a forma do array)
contador = np.arange(10)
print(contador)
print(contador.reshape(5, 2)) # order = 'C'
print(contador.reshape((5, 2), order = 'F'))

# Altera a forma e o tamanho do array
dados_new = dados.copy()
dados_new = np.resize(dados_new, (3, 5))
print(dados_new)

dados_new[2] = dados_new[0] / (2023 - dados_new[1])
print(dados_new)
