# Escreva um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
cidade = input('Em que cidade você nasceu? ').strip()
print(cidade[:5].upper() == 'SANTO')
# Outra forma de fazer
cidade = cidade.split()
print(cidade[0].upper() == 'SANTO')
# Outra forma de fazer
print('SANTO' in cidade[0].upper())