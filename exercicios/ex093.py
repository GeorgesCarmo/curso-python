# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa deverá ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso deverá ser guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
total_gols = 0
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    total_gols += gols[i]
jogador['gols'] = gols.copy()
jogador['total'] = total_gols
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
print(f'Os gols foram: {gols}')
print(f'O total de gols foi {total_gols}.')
print('-=' * 20)
print(f'Analisando os dados...')
for i, v in enumerate(gols):
    print(f'Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {total_gols} gols.')
print('-=' * 20)
print('Fim do programa.')
