# Isto é um comentário de uma linha

'''
Isto é um comentário 
de mais
de uma 
linha
'''

# str.format()
print('Olá, {}. Tudo bem com você?'.format('Jovem'))
print('Parabéns, {}! Você foi classificado na posição de número {}.'.format('Fulano', 24))
print('Parabéns, {nome}! Você foi classificado na posição de número {posicao}.'.format(nome='Fulano', posicao=24))

# f-Strings
nome='Fulano'
posicao=24
print(f'Parabéns, {nome}! Você foi classificado na posição de número {posicao}.')
