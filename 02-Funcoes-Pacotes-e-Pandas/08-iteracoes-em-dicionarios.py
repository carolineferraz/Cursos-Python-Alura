dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

# Retornar uma lista contendo as chaves do dicionário
print(dados.keys())

for key in dados.keys():
    print(dados[key])


# Retornar uma lista contendo os valores do dicionário
print(dados.values())


# Retornar uma lista contendo uma tupla para cada par chave-valor do dicionário
print(dados.items())

for item in dados.items():
    print(item)

for key, value in dados.items():
    print(key, value)

for key, value in dados.items():
    if value > 100000:
        print(key, value)