dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

# Atualizar o dicionário, adicionando um ou mais itens chave/valor ou modificando o valor de um item existente
dados.update({'DS5': 124549.07})
print(dados)
dados.update({'DS5': 120500.0})
print(dados)
dados.update({'Fusca': 100250.0, 'Camaro': 200800.85})
print(dados)

# Criar uma cópia do dicionário
dadosCopy = dados.copy()
del dadosCopy['Fusca']
print(dadosCopy)
print(dados)

# Se a chave for encontrada no dicionário, o item é removido e seu valor é retornado. Caso contrário, o valor especificado como default é retornado. Se o valor default não for fornecido e a chave não for encontrada no dicionário um erro será gerado
print(dados.pop('Passat'))
print(dados)
print(dados.pop('Passat', 'Chave não encontrada'))

# Limpar o dicionário
dados.clear()
print(dados)