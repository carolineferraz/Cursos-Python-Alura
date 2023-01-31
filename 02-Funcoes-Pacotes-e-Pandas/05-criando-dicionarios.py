carros = ['Jetta Variant', 'Passat', 'Crossfox']
valores = [88078.64, 106161.94, 72832.16]

print(carros.index('Passat'))

print(valores[carros.index('Passat')])

# Os mesmos dados em um formato de dicionário:
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
print(dados)
print(type(dados))


# Criando um dicionário com zip():
# print(list(zip(carros, valores)))
dict(zip(carros, valores))
print(dados)