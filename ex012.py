# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira.
from math import trunc
num = float(input('Digite um número real: '))
print('A parte inteira de {} é {}'.format(num, trunc(num)))