import pandas as pd

dataset = pd.read_csv('02-Funcoes-Pacotes-e-Pandas/data/db.csv', sep=';', index_col=0)

print(dataset.head())

print("-"*100)

print("Para iterar com DataFrames podemos utilizar o método iterrows(), que retorna uma tupla contendo o índice da linha do DataFrame e uma Series contendo as informações referentes a esse índice\n")
# print(list(dataset.iterrows()))

print("Podemos utilizar o método iterrows() num laço for para iterar sobre cada uma das linhas do DataFrame. Segue um exemplo onde iteramos sobre as linhas do DF para adicionar uma uma coluna com a quilometragem média anual de cada veículo: \n")

for index, linha in dataset.iterrows():
    if(2019 - linha['Ano'] != 0):
        dataset.loc[index, 'Km_media'] = round(linha['Quilometragem'] / (2019 - linha['Ano']))
    else:
        dataset.loc[index, 'Km_media'] = 0

print(dataset)