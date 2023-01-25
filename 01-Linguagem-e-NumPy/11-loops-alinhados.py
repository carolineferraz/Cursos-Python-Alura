dados = [['Rodas de liga', 'Travas elétricas', 'Ar condicionado', 'Sensor de Distância', 'Bancos de Couro'], ['Freio Automático', 'Travas elétricas', 'Suspensão Hidráulica', 'Sensor de Distância', '4 X 4'], ['Rodas de liga', '4 X 4', 'Ar condicionado', 'Bancos de Couro', 'Freio Automático']]

# Para imprimir as listas dentro da lista dados
for lista in dados:
    print(lista)

# Para imprimir os itens dentro das listas dentro da lista dados
for lista in dados:
    for item in lista:
        print(item)

# Para criar uma lista Acessorios com os itens das listas dentro da lista dados
Acessorios = []

for lista in dados:
    for item in lista:
        Acessorios.append(item)

print(Acessorios)

# Para remover os itens duplicados da lista Acessorios e imprimi-la
print(list(set(Acessorios)))

# Para, em uma únida linha, criar uma lista com os itens da lista dados, remover o itens duplicados e imprimir a lista
print(list(set([item for lista in dados for item in lista])))