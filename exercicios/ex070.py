# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
from time import sleep
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('=-' * 30)
print('Gerando 5 números aleatórios...')
sleep(2)
print(f'Os números gerados foram: {numeros}')
print('=-' * 30)
print(f'O maior número gerado foi {max(numeros)}')
print(f'O menor número gerado foi {min(numeros)}')