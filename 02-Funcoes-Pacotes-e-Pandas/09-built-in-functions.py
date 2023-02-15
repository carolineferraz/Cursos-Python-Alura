dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

# somando os valores do dicionário dados
valores = []

for valor in dados.values(): # esse for também poderia ser um list(dados.values())
    valores.append(valor)

print(valores)

soma_valores = 0

for item in valores:
    soma_valores += item

print(soma_valores)

# agora, fazendo a mesma coisa só que com a buil-in function sum()
print(sum(dados.values()))