# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}.'.format(frase.find('A') + 1))
print('A última letra A aparece na posição {}.'.format(frase.rfind('A') + 1))
# Outra forma de fazer
# print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
# print('A primeira letra A aparece na posição {}.'.format(frase.index('A') + 1))
# print('A última letra A aparece na posição {}.'.format(frase.rindex('A') + 1))
# Outra forma de fazer
# print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
# print('A primeira letra A aparece na posição {}.'.format(frase.find('A') + 1))
# print('A última letra A aparece na posição {}.'.format(frase.rfind('A') + 1))
# Outra forma de fazer
# print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
# print('A primeira letra A aparece na posição {}.'.format(frase.index('A') + 1))    
# print('A última letra A aparece na posição {}.'.format(frase.rindex('A') + 1))