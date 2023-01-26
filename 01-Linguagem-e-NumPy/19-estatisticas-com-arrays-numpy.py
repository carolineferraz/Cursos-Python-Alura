import numpy as np;

anos = np.loadtxt('01-Linguagem-e-NumPy/data/carros-anos.txt', dtype=int)
km = np.loadtxt('01-Linguagem-e-NumPy/data/carros-km.txt')
valor = np.loadtxt('01-Linguagem-e-NumPy/data/carros-valor.txt')

print(anos.shape)
print(km.shape)
print(valor.shape)

# Retorna um array multidimensional a partir de vários (dois ou mais) arrays de uma única dimensão
dataset = np.column_stack((anos, km, valor))
print(dataset)
print(dataset.shape)

# Retorna a média dos elementos do array ao longo do eixo especificado
print(np.mean(dataset, axis=0))
print(np.mean(dataset[ : , 1]))
print(np.mean(dataset[ : , 2]))

# Retorna o desvio padrão dos elementos do array ao longo de um eixo especificado
print(np.std(dataset[ : , 2]))

# Retorna a soma dos elementos do array ao longo de um eixo especificado
print(dataset.sum(axis=0))
print(dataset[ : , 1].sum())

print(np.sum(dataset, axis=0))
print(np.sum(dataset[ : , 1]))
