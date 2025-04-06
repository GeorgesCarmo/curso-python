# Condições aninhadas

# Condições aninhadas são condições dentro de outras condições. Elas são usadas para verificar múltiplas condições em sequência.

nome = input('Qual é o seu nome? ')
if nome == 'Georges':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))