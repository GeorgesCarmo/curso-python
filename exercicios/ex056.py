# Crie um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

import math
numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = math.factorial(numero)
print('Calculando {}! = '.format(numero), end='')
# Ou
for i in range(numero, 0, -1):
    print(f'{i}', end='')
    if i == 1:
        print(' = ', end='')
    else:
        print(' x ', end='')
print(f'{fatorial}')

# Ou
numero = int(input('Digite um número para calcular seu fatorial: '))
contador = numero
fatoria = 1
print('Calculando {}! = '.format(numero), end='')
while contador > 0:
    print('{} '.format(contador), end='')
    print('x' if contador > 1 else '=', end=' ')
    fatoria *= contador
    contador -= 1
print('{}'.format(fatoria))    
