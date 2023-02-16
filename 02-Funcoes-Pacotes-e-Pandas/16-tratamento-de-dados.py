import pandas as pd

dataset = pd.read_csv('02-Funcoes-Pacotes-e-Pandas/data/db.csv', sep=';', index_col=0)

print(dataset.head())

print("-"*100)

print("\nUma forma rápida de verificar informações sobre um dataset é utilizando o método info():\n")
print(dataset.info())

print("-"*100)

print("\nNós podemos utilizar o método isna() sobre uma coluna do DF para retornar uma Series de valores booleanos contendo True para valores nulos e False para valores não-nulos:\n")
print(dataset.Quilometragem.isna())

print("-"*100)

print("\nPodemos também fazer um select das linhas do DF que contém os valores de uma coluna específica igual a nulo:\n")
print(dataset[dataset.Quilometragem.isna()])

print("-"*100)

print("\nUma forma rápida de substituir esses valores nulos por algum valor específico e já aplicar esses valores ao DF é utilizando o método fillna(valor, inplace=True):\n")
dataset.fillna(0, inplace=True)
print(dataset)

print("-"*100)

print("\nTambém é possível eliminar as linhas que contêm coluna com valor nulo e já atribuir essa alteração ao dataset a partir do método dropna():\n")
dataset = pd.read_csv('02-Funcoes-Pacotes-e-Pandas/data/db.csv', sep=';', index_col=0)
dataset.dropna(subset = ['Quilometragem'], inplace = True)
print(dataset)