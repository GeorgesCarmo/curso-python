# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
print('Valores sorteados: ')
for i in range(1, 5):
    jogadores[f'Jogador {i}'] = randint(1, 6)
    print(f'Jogador {i} tirou {jogadores[f"Jogador {i}"]}')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('    == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
print('-=' * 20)
print('    == FIM DO JOGO ==')
