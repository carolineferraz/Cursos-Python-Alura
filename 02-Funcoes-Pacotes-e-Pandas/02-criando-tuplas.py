# Tuplas são sequências imutáveis que são utilizadas para armazenar coleções de itens, geralmente heterogêneos. As tuplas podem ser construídas de várias formas:

# utilizando um par de parênteses
Carro = () 

# utilizando uma vírgula à direita
Carro = 15000, 800

# utilizando um par de parênteses con itens separados por vírgula
Carro = (15000, 800)

nome = 'Passat'
valor = 153000
Carro = (nome, valor)
print(Carro)

# utilizando tuple() ou tuple(iterator)
['Jetta Variant', 'Passat', 'Crossfox', 'DSS']
nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
print(nomes_carros)

print(type(nomes_carros))