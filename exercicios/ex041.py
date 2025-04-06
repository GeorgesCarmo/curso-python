# Crie um programa que faça o computador jogar jokenpo com vocé.
from random import randint
from time import sleep
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('Qual é a sua jogada? '))
if jogador < 0 or jogador > 2:
    print('Jogada inválida! Tente novamente.')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('-=-' * 20)
    computador = randint(0, 2)
    print('O computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=-' * 20)
    if jogador == 0 and computador == 2:
        print('VITÓRIA!')
    elif jogador == 1 and computador == 0:
        print('VITÓRIA!')
    elif jogador == 2 and computador == 1:
        print('VITÓRIA!')
    else:
        print('DERROTA!')