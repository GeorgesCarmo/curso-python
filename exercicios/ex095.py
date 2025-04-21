# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []
jogador = dict()
gols = []
total = 0
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
        total += gols[i]
    jogador['gols'] = gols.copy()
    jogador['total'] = total
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    total = 0
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if continuar == 'N':
        break 
print('-=' * 20)
print('Analisando os dados...')
print('-=' * 20)
print('cod', f'{"nome":<15}', f'{"gols":<15}', f'{"total":<15}')
print('-' * 45)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 45)
while True:
    busca = int(input('Deseja ver os dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
        print('-=' * 45)
       
