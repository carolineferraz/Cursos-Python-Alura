Acessorios = ['Rodas de liga', 'Travas elétricas', 'Ar condicionado', 'Sensor de Distância', 'Bancos de Couro']

# A.sort() (ordena os itens da lista A)
Acessorios.sort()
print(Acessorios)

# A.append(x) (adiciona um elemento x ao final da lista A)
Acessorios.append('4 x 4')
print(Acessorios)

# A.pop(i) (remove e retorna o elemento de índice i da lista A. se não forem passados parâmetros o pop() remove e retorna o último item da lista)
Acessorios.pop()
print(Acessorios)
Acessorios.pop(2)
print(Acessorios)

# A.copy() (cria uma nova área na memória com uma lista idêntica à lista A)
Acessorios_2 = Acessorios.copy()
Acessorios_2.append('4 x 4')
print(Acessorios)
print(Acessorios_2)