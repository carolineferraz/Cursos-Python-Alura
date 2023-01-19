Acessorios = ['Rodas de liga', 'Travas elétricas', 'Ar condicionado', 'Sensor de Distância', 'Bancos de Couro']

# A[i] (acessa o i-ésimo item da lista A)
print(Acessorios[0])
print(Acessorios[2])

# A[-1] (acessa o última item da lista A)
print(Acessorios[-1])
print(Acessorios[-2])

# A[i][i] (acessa o item de índice i dentro de umaa lista que está no índice i da lista A)
Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 5712.00, False, ['Piloto Automático', 'Teto Panorâmico', 'Rodas de Liga'], 8824.66]
print(Carro_1[5][0])

Carros = [Carro_1, None, None]
print(Carros[0][5][0])

# A[i:j] (acessa a lista A recortando-a do índice i até o índice j. o elemento com índice i é incluído e o elemento com índice j não é incluído)

print(Carro_1[2 : 5])
print(Carro_1[2 : -1])
print(Carro_1[2 :])
print(Carro_1[:2])