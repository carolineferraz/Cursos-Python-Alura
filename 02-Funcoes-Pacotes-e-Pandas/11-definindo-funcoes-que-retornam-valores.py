def media_2(valor_1, valor_2, valor_3):
    media = (valor_1 + valor_2 + valor_3) / 3
    return media

print(media_2(1,2,3))

def media_3(lista):
    media = sum(lista) / len(lista)
    return media

print(media_3([1,2,3]))

# retornando mais de um valor:
def media_4(lista):
    media = sum(lista) / len(lista)
    return media, len(lista)

print(media_4([1,2,3]))


# Exercício:
# Dado o dataset abaixo, faça uma função que cria um dicionário com a média de km rodados anual de cada veículo

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def cria_dict_media_km(dataset, km_atual):
    resultado = {}
    for item in dataset.items():
        media_km = round(item[1]['km'] / (km_atual - item[1]['ano']), 2)
        resultado.update({ item[0]: media_km })
    return resultado

print(cria_dict_media_km(dados, 2023))


# Exercício:
# Dado o dataset abaixo, faça uma função que adiciona ao dicionário a média de km rodados anual de cada veículo

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def adiciona_media_km(dataset, km_atual):
    for item in dataset.items():
        media_km = round(item[1]['km'] / (km_atual - item[1]['ano']), 2)
        item[1]['km_media'] = media_km
    return dataset

print(adiciona_media_km(dados, 2023))