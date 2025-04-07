# Melhore o jogo da adivinhação, onde o computador vai "pensar" em um número entre 0 e 10. O jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

import random

def jogo_adivinhacao():
    computador = random.randint(0, 10)
    acertou = False
    palpites = 0
    while not acertou:
        jogador = int(input('Em que número eu pensei? '))
        palpites += 1
        if jogador == computador:
            acertou = True
        else:
            if jogador < computador:
                print('Mais... Tente novamente.')
            elif jogador > computador:
                print('Menos... Tente novamente.')
    print('Acertou com {} palpites!'.format(palpites))

jogo_adivinhacao()