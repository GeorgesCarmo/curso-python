# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os 4 últimos colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

time = ('Botafogo', 'Grêmio', 'Fluminense', 'São Paulo', 'Palmeiras', 'Atlético-MG', 'Internacional', 'Corinthians',
        'Santos', 'Athletico-PR', 'Fortaleza', 'Ceará', 'Bahia', 'Vasco', 'Cruzeiro', 'Atlético-GO',
        'Coritiba', 'Goiás', 'Bragantino', 'Chapecoense')
print('=-' * 30)
print(f'Lista de times do Brasileirão: {time}')
print('=-' * 30)
print(f'Os 5 primeiros colocados: {time[0:5]}')
print('=-' * 30)
print(f'Os 4 ultimos colocados: {time[-4:]}')
print('=-' * 30)
print(f'Times em ordem alfabetica: {sorted(time)}')
print('=-' * 30)
print(f'Chapecoense esta na {time.index("Chapecoense") + 1}a posicao')