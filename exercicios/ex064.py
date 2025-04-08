# Faça um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Vocês jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÉ VENCEU!')
            vitorias += 1
        else:
            print('VOCÉ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÉ VENCEU!')
            vitorias += 1
        else:
            print('VOCÉ PERDEU!')
            break
print(f'GAME OVER! Vocês venceu {vitorias} vezes.')