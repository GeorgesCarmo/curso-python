# Faça um programa que ajude um jogador da mega sena a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample
from random import randint
jogos = []
quantidade = int(input('Quantos jogos vocé quer que eu sorteie? '))
for i in range(0, quantidade):
    jogos.append(sample(range(1, 61), 6))
for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}')

print('=-' * 30)

lista = list()
jogos = list()
print('-' * 30)
print('Sorteando 6 números para você...')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
totalJogos = 1
while totalJogos <= quant:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totalJogos += 1
print(f'Sorteando {quant} jogos...')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
print('-=' * 30)
print('Boa sorte!')      
   