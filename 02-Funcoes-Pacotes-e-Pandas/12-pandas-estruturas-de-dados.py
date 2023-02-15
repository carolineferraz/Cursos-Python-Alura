import pandas as pd

# Series: 
# Series são arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado. Os rótulos das linhas são chamados de index. A forma básica de criação de uma Series é a seguinte (onde o parâmetro dados pode ser um dicionário, uma lista, um array numpy ou até uma constante):

# s = pd.Series(dados, index=index)


# DataFrames:
# DataFrame é uma estrutura de dados tabular bidimensional com rótulos nas linhas e nas colunas. Como as Series, os DataFrames são capazes de armazenar qualquer tipo de dado. A forma básica de criação de um DataFrame é a seguinte (onde o parâmetro dados pode ser um dicionário, uma lista, um array numpy ou até uma constante):

# df = pd.DataFrame(dados, index=index, columns=colums)


print("Criando uma Series a partir de uma lista:\n")
carros = ['Jetta Variant', 'Passat', 'Crossfox']
s = pd.Series(carros)
print(s)

print("-"*100)


print("Criando um DataFrame a partir de uma lista de dicionários:\n")
dados = [
    { 'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64 },
    { 'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94 },
    { 'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16 }
]

df = pd.DataFrame(dados)
print(df)

print("-"*100)


print("Se você quiser modificar a ordem em que as colunas aparecem você pode fazer o seguinte:\n")
df[['Nome', 'Valor', 'Ano', 'Quilometragem', 'Motor', 'Zero_km']]
print(df)

print("-"*100)


print("Criando um DataFrame a partir de um dicionário:\n")
dados = { 
    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'],
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Ano': [2003, 1991, 1990],
    'Quilometragem': [44410.0, 5712.0, 37123.0],
    'Zero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}

df = pd.DataFrame(dados)
print(df)

print("-"*100)


print("Criando um DataFrame a partir de arquivos externos:\n")

df = pd.read_csv('02-Funcoes-Pacotes-e-Pandas/data/db.csv', sep=';')
print(df)