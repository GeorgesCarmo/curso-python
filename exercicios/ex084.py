# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

totalPessoas = 0
pessoas = []
maiorPeso = 0
menorPeso = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])
    totalPessoas += 1
    if totalPessoas == 1:
        maiorPeso = menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {totalPessoas} pessoas.')
print(f'O maior peso foi de {maiorPeso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menorPeso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'[{p[0]}]', end=' ')
print()