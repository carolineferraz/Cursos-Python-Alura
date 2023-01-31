nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')

print('Iterações com tuplas: ')
for item in nomes_carros:
    print(item)


print('\nDesempacotamento de tuplas: ')
carro_1, carro_2, carro_3, carro_4 = nomes_carros
print(carro_1)
print(carro_2)
print(carro_3)
print(carro_4)


print('\nDesempacotamento de tuplas: ')
_, A, _, B = nomes_carros
print(A)
print(B)


print('\nDesempacotamento de tuplas: ')
_, B, *_ = nomes_carros
print(B)


print('\nUtilizando o iterador zip() para realizar iterações em paralelo')
carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
valores = [88078.64, 106161.94, 72832.16, 124549.07]
print(list(zip(carros, valores)))
# desta forma, foi criada uma lista de tuplas onde cada tupla contendo dois itens equidistantes de cada um ods arrays (carros e valores)

print('\nMais exemplos de iterações utilizando o zip()')
for carro, valor in zip(carros, valores):
    print(carro, valor)

print('\nUtilizando o if')
for carro, valor in zip(carros, valores):
    if(valor > 100000):
        print(carro)