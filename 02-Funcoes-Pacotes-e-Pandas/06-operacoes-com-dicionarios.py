dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

# Retornando o valor de uma chave específica: 
print(dados['Passat'])

# Verificando se uma chave existe ou não existe em um dicionário:
print('Passat' in dados)
print('Fusca' in dados)
print('Passat' not in dados)
print('Fusca' not in dados)

# Verificando o número de pares chave/valor:
print(len(dados))

# Adicionando um item ao dicionário:
dados['DS5'] = 124549.07
print(dados)

# Removendo um par chave/valor:
del dados['Passat']
print(dados)