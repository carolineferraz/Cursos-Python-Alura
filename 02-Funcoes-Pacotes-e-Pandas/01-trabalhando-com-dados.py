import pandas as pd

dataset = pd.read_csv('02-Funcoes-Pacotes-e-Pandas/data/db.csv', sep = ';')
# pd.set_option('display.max_rows', 1000)
# pd.set_option('display.max_columns', 1000)

print(dataset)

print(dataset.dtypes)

print(dataset[['Quilometragem', 'Valor']].describe())

print(dataset.info())