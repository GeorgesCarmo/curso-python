# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
for c in range(0, 5):
    numeros.append(int(input(f'Digite o {c + 1} número: ')))
print(f'Os valores digitados foram: {numeros}')
print(f'O maior valor digitado foi {max(numeros)} e ele se encontra na posição ', end='')
for i, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{i}...', end='')
print()        
print(f'O menor valor digitado foi {min(numeros)} e ele se encontra na posição ', end='')
for i, v in enumerate(numeros):
    if v == min(numeros):
        print(f'{i}...', end='')
print()
