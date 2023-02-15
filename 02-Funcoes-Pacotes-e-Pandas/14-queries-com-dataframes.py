import pandas as pd

dataset = pd.read_csv('02-Funcoes-Pacotes-e-Pandas/data/db.csv', sep=';', index_col=0)

print(dataset.head())

print("-"*100)

print("\nPara retornar uma Series com as informações da coluna 'Motor'")
print(dataset.Motor)

print("-"*100)

print("\nPara retornar uma Series com um boolean que informa se o valor da coluna 'Motor' é igual a 'Motor Diesel'")
print(dataset.Motor == 'Motor Diesel')

print("-"*100)

print("\nUma forma interessante de se trabalhar com esse retorno booleano é atribuir a Series retornada a uma variável e utilizá-la como parâmetro para selecionar linhas do DataFrame. Veja como retornar apenas as linhas do DF que contêm o valor da coluna 'Motor' igual a 'Motor Diesel':")
select = dataset.Motor == 'Motor Diesel'
print(dataset[select])

print("-"*100)

print("\nAgora, vamos supor que fosse necessário retornar um DataFrame com apenas as linhas que contêm o valor da coluna 'Motor' igual a 'Motor Diesel' e também que contêm o valor da coluna 'Zero_km' igual a True. Ficaria assim:")
print(dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)])

print("-"*100)

print("\nPodemos fazer a mesma seleção que fizemos acima utilizando um 'método query', uma maneira também bem bacana de se fazer seleções em DataFrames, que simula queries do banco de dados. Ficaria assim:")
print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))