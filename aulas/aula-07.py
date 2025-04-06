# Cores no terminal
import os
os.system('cls')
print('\033[1;31mOla, Mundo!\033[m')    # Vermelho
print('\033[1;32mOla, Mundo!\033[m')    # Verde
print('\033[1;33mOla, Mundo!\033[m')    # Amarelo
print('\033[1;34mOla, Mundo!\033[m')    # Azul
print('\033[1;35mOla, Mundo!\033[m')    # Roxo
print('\033[1;36mOla, Mundo!\033[m')    # Ciano
print('\033[1;37mOla, Mundo!\033[m')    # Cinza

print('*' * 50)

# Background
print('\033[41mOla, Mundo!\033[m')      # Vermelho
print('\033[42mOla, Mundo!\033[m')      # Verde
print('\033[43mOla, Mundo!\033[m')      # Amarelo
print('\033[44mOla, Mundo!\033[m')      # Azul
print('\033[45mOla, Mundo!\033[m')      # Roxo
print('\033[46mOla, Mundo!\033[m')      # Ciano
print('\033[47mOla, Mundo!\033[m')      # Cinza

print('*' * 50)

# Estilos
print('\033[1mOla, Mundo!\033[m')       # Negrito
print('\033[4mOla, Mundo!\033[m')       # Sublinhado
print('\033[7mOla, Mundo!\033[m')       # Invertido
print('\033[8mOla, Mundo!\033[m')       # Oculto
print('\033[9mOla, Mundo!\033[m')       # Tachado
print('\033[0mOla, Mundo!\033[m')       # Limpa

print('*' * 50)

nome = 'Georges'
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;30m',
    'verde': '\033[32m',
    'vermelho': '\033[31m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!!'.format(cores['amarelo'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!!'.format(cores['azul'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!!'.format(cores['pretoebranco'], nome, cores['limpa']))