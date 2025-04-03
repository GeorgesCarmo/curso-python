# Utilizando modulos
import math
import random
import emoji
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))

print('-' * 50)
# O que é um módulo?
# Um módulo é um arquivo que contém definições e instruções Python.
# O arquivo pode conter funções, classes e variáveis que podem ser reutilizadas em outros programas.
# O que é um pacote?
# Um pacote é uma coleção de módulos organizados em diretórios.
# O que é um namespace?
# Um namespace é um espaço onde os nomes das variáveis, funções e classes são armazenados.
# O que é um escopo?
# Um escopo é uma região do código onde um nome é reconhecido.
# O que é um escopo local?
# Um escopo local é o escopo de uma função ou método.
# O que é um escopo global?
# Um escopo global é o escopo do módulo.
# O que é um escopo built-in?
# Um escopo built-in é o escopo de funções e variáveis internas do Python.

print(random.randint(1, 100))
# O que é um módulo padrão?
# Um módulo padrão é um módulo que vem junto com o interpretador Python.

print('-' * 50)
# Ambiente virtual para instalação de pacotes
""""
python3 -m venv meu_ambiente
source meu_ambiente/bin/activate
pip install emoji"
"""
# Para sair do ambiente virtual: deactivate
# https://www.webfx.com/tools/emoji-cheat-sheet/

print(emoji.emojize('Olá :smile:', language='alias'))
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Vamos jogar :game_die:'))
print(emoji.emojize('Python é :snake:'))

