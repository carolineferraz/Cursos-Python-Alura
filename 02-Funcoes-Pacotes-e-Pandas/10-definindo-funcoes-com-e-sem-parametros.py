def media():
    media = (1 + 2 + 3) / 3
    print(media)

def media_2(valor_1, valor_2, valor_3):
    media = (valor_1 + valor_2 + valor_3) / 3
    print(media)

def media_3(lista):
    media = sum(lista) / len(lista)
    print(media)


# Exercício:
# Dado o dataset abaixo, faça uma função que calcula a média de km rodados anual de cada veículo

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def calcula_media_km(dataset, km_atual):
    for item in dataset.items():
        media_km = item[1]['km'] / (km_atual - item[1]['ano'])
        print(media_km)

calcula_media_km(dados, 2023)