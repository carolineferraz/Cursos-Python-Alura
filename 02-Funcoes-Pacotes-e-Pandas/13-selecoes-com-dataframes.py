import pandas as pd

dataset = pd.read_csv('02-Funcoes-Pacotes-e-Pandas/data/db.csv', sep=';', index_col=0)

print('Para retornar os 5 primeiros registros do DataFrame:\n')
print(dataset.head())


print("-"*100)


print('Para retornar uma coluna específica do DataFrame:\n')
print(dataset['Valor'])

print("-"*100)

print('\nNote que agora que quando você retorna uma única coluna do DF esse dado será uma Series:\n')
print(type(dataset['Valor']))

print("-"*100)

print('\nSe nós quisermos retornar uma única coluna do DF mantendo o tipo de dado como DF podemos fazer o seguinte:\n')
print(dataset[['Valor']])
print(type(dataset['Valor']))

print("-"*100)

print('\nPara fazer um slice nas linhas do DF:\n')
print(dataset[0:3])

print("-"*100)

print('\nO loc() seleciona linhas e colunas segundo os rótulos de uma matriz booleana.')
print('\nPara selecionar toda a linha que possui o nome "Passat":\n')
print(dataset.loc['Passat'])

print("-"*100)

print('\nRepare que o dado foi retornado no formato de Series. Para retornar no formato de DF basta colocar dois colchetes. Se você quiser retornar as linhas que possuem o nome "Passat" e "Crossfox" ficaria assim:\n')
print(dataset.loc[['Passat', 'Crossfox']])

print("-"*100)

print("Lembrando que configuraos nosso DF para ter os nomes como sendo os 'rótulos'")

print("-"*100)

print('\nAgora, se quisermos retornar apenas as colunas "Motor" e "Valor" das linhahs que possuem como rótulo (o nome) "Passat" e "Crossfox" fazemos assim:\n')
print(dataset.loc[['Passat', 'Crossfox'], ['Motor', 'Valor']])

print("-"*100)

print('\nAgora, se quisermos retornar apenas as colunas "Motor" e "Valor" de todas as linhas podemos fazer assim:\n')
print(dataset.loc[ : , ['Motor', 'Valor']])

print("-"*100)

print('\nO iloc() seleciona com base nos índices, ou seja, se baseia nas posições das informações.')
print('\nPara selecionar toda a linha que possui do índice 1 ("Passat"):\n')
print(dataset.iloc[1])

print("-"*100)

print('\nRepare que o tipo de dado foi retornado como Series. Para fazer a mesma coisa retornando o tipo de dado como DF:\n')
print(dataset.iloc[[1]])

print("-"*100)

print('\nPara selecionar todas as linhas do índice 1 ao 3:\n')
print(dataset.iloc[1:4])
print(type(dataset.iloc[1:4]))

print("-"*100)

print('\nPara selecionar colunas específicas todas as linhas do índice 1 ao 3 (por exemplo), primeiro fazemos os slice das linhas e depois especificamos as colunas, assim:\n')
print(dataset.iloc[1:4, [1, 5, 4]])

print("-"*100)

print('\nTambém é possível selecionar colunas específicas de linhas específicas de forma parecida, por exemplo assim:\n')
print(dataset.iloc[[3, 21, 28], [1, 5, 4]])
