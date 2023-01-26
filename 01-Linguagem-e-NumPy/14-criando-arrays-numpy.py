import numpy as np 
# 'as np' serve para dar um apelido à biblioteca importada. não é obrigatório mas é interessante usar 
# taambém é possível não importar a biblioteca inteira e sim apenas algo específico da biblioteca que você quer usar. Exemplo: from numpy import arange

# A função arange cria um arranjo contendo uma seqüência de valores especificados em um intervalo com início e fim dados
print(np.arange(10)) 

# Criando arrays numpy:
km = np.array([1000, 2300, 4987, 1500])
print(km)

print(type(km))
print(km.dtype)
print(km.shape)


dados = [
    ["Jetta Variant", 2003, False],
    ["Passat", 1991, False],
    ["Crossfox", 1990, False],
    ["DSS", 2019, True],
    ["Aston Martin DB4", 2006, False],
    ["Palio Weekend", 2012, False],
    ["A5", 2019, True],
    ["Serie 3 Cabrio", 2009, False],
    ["Dodge Jorney", 2019, False],
    ["Carens", 2011, False],
]

Acessorios = np.array(dados)

print(Acessorios)
print(Acessorios.shape)