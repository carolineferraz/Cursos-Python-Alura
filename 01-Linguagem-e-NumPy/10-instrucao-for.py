Acessorios = ['Rodas de liga', 'Travas elétricas', 'Ar condicionado', 'Sensor de Distância', 'Bancos de Couro']

for item in Acessorios:
    print(item)

# range()
print(list(range(10)))

for i in range(10):
    print(i ** 2)

# laço for com range
quadrado = []

for i in range(10):
    quadrado.append(i ** 2)

print(quadrado)

# laço for com range numa única linha
print([i ** 2 for i in range(10)])

