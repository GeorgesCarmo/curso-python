# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#  O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
computador = random.randint(0, 5)  # Faz o computador pensar em um número entre 0 e 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
sleep(2)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
print('-=-' * 20)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))
print('Fim do programa!')